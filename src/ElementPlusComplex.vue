<template>
  <el-card class="box-card" shadow="hover"
    style="margin: 20px;"
    v-if="showCard" :data-testid="'d674d5c3-1333-497f-b41f-c627752eab2e'">
    <el-divider direction="horizontal" content-position="left" :data-testid="'7698bbaf-5d46-446b-8ebb-8659e09c9cb4'"/>
    <div slot="header" class="clearfix">
      <span>Complex Card</span>
      <el-button style="float: right;" size="mini" :data-testid="'72a5c2ce-92fd-4027-8e62-00b97e9b535b'">Action</el-button>
    </div>
    <el-row gutter="20" :data-testid="'dcd7ea2e-0b8c-4c21-b71a-049cee1c665c'">
      <el-col :span="8" :data-testid="'37d2cf91-dbae-477e-b0d1-36201543c3ff'">
        <el-input
          v-model="inputValue"
          placeholder="Enter text"
          clearable
          maxlength="50" :data-testid="'d6612398-e344-41d4-bcef-ef4ef575dfb1'"/>
        <el-divider :data-testid="'f017d7a0-5599-4723-b912-92df2ef611e5'"/>
      </el-col>
      <el-col :span="8" :data-testid="'185fbd46-e656-40b2-9529-4e34b8d6f0f6'">
        <el-select v-model="selected" placeholder="Select" :data-testid="'2a3b28c4-f485-4a43-b8bf-0ee5096a178e'">
          <el-option label="Option 1" value="1" :data-testid="'917e830e-a1e7-4c1a-af60-ae5240c1df64'"/>
          <el-option label="Option 2" value="2" :data-testid="'255f323b-a433-433f-bee9-960dcbb0b103'"/>
        </el-select>
        <el-divider direction="vertical" :data-testid="'e0605247-e6ca-4d9d-b234-bf819a966355'"/>
      </el-col>
      <el-col :span="8" :data-testid="'ef728a37-606f-4c8f-add2-c7f8cfeb24d9'">
        <el-date-picker
          v-model="date"
          type="date"
          placeholder="Pick a date"
          format="yyyy-MM-dd" :data-testid="'02bf4cf8-35e7-4bee-a3c9-52325af4f6d5'"/>
        <el-divider :data-testid="'d8bf5cc5-3374-4dce-b8c3-9b543e7ad8b6'"/>
      </el-col>
    </el-row>
    <el-alert
      title="This is a success alert"
      type="success"
      show-icon
      :closable="false"
      description="More details here." :data-testid="'ab348ef3-c270-4283-b83d-022fd3a4d65e'"/>
  </el-card>
</template>

<script>
export default {
  data() {
    return {
      showCard: true,
      inputValue: '',
      selected: '',
      date: null
    }
  }
}
</script>

<style scoped>
.box-card {
  width: 800px;
}
</style>
