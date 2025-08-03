
import re
import uuid
import glob
import os

used_uuids = set()

def get_unique_uuid():
    while True:
        new_id = str(uuid.uuid4())
        if new_id not in used_uuids:
            used_uuids.add(new_id)
            return new_id

def add_datatest_to_vue(vue_content):
    def replacer(match):
        tag = match.group(1)
        attrs = match.group(2)
        closing = match.group(3)
        unique_id = get_unique_uuid()
        if ':data-testid' not in attrs:
            attrs = attrs.rstrip() + f' :data-testid="\'{unique_id}\'"'
        return f'<{tag}{attrs}{closing}'
    pattern = r'<(el-[a-zA-Z0-9\-]+)([\s\S]*?)(/?>)'
    return re.sub(pattern, replacer, vue_content, flags=re.DOTALL)

if __name__ == "__main__":
    vue_dir = "src"
    vue_files = glob.glob(os.path.join(vue_dir, "*.vue"))
    for vue_file in vue_files:
        with open(vue_file, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = add_datatest_to_vue(content)
        with open(vue_file, "w", encoding="utf-8") as f:
            f.write(new_content)
