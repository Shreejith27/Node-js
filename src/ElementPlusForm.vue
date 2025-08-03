<template>
  <el-form :model="form" label-width="120px" :data-testid="'57ac6fb3-e8a8-4e42-84ab-757b1bcd4520'">
    <el-form-item label="Name" :data-testid="'142dd332-180f-41a2-add7-1a51cdfd517a'">
      <el-input v-model="form.name" :data-testid="'102f7ad7-3be4-4c80-a8a9-232bb70469cc'"/>
    </el-form-item>
    <el-form-item label="Email" :data-testid="'7b50d2a2-77a9-49bd-bfb1-4cf358e89700'">
      <el-input v-model="form.email" :data-testid="'cdc9772d-67d8-45d0-b2a7-ec0550b2e634'"/>
    </el-form-item>
    <el-form-item label="Gender" :data-testid="'4e6a5bdf-0145-48bc-8343-1671c2cabafd'">
      <el-radio-group v-model="form.gender" :data-testid="'859ef5ea-3fee-4667-908a-69c88fe6bd3d'">
        <el-radio label="Male" :data-testid="'54c2e14c-2712-4696-ab3f-4a44c3bf7122'"/>
        <el-radio label="Female" :data-testid="'9b44e3df-253e-4490-a9dd-668f0bba64b9'"/>
      </el-radio-group>
    </el-form-item>
    <el-form-item :data-testid="'69ae4a47-7ccc-41cf-a426-36f2ac0531f0'">
      <el-button type="primary" :data-testid="'2a6fd7cf-7a0f-4b31-9158-2e077a6fa3a1'">Submit</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
export default {
  data() {
    return {
      form: {
        name: '',
        email: '',
        gender: ''
      }
    }
  }
}
</script>
