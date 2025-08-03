<template>
  <el-dialog title="Dialog Title" :visible.sync="visible" :data-testid="'aa935836-b874-4851-8d87-1c24c23e740c'">
    <span>This is a dialog content.</span>
    <template #footer>
      <el-button @click="visible = false" :data-testid="'f6cab652-72e2-4e28-b797-f05b37edf4aa'">Cancel</el-button>
      <el-button type="primary" @click="visible = false" :data-testid="'dfa21b85-24dc-4514-86eb-67e4197e8123'">OK</el-button>
    </template>
  </el-dialog>
  <el-button @click="visible = true" :data-testid="'bf9e808f-4842-43f7-97f0-0658ced96ba3'">Open Dialog</el-button>
</template>

<script>
export default {
  data() {
    return {
      visible: false
    }
  }
}
</script>
