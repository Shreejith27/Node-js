<template>
  <el-table :data="tableData" style="width: 100%" :data-testid="'7de4f6f6-ab8d-4b9e-bfb2-69069c6aae98'">
    <el-table-column prop="date" label="Date" width="180" :data-testid="'0d3aa455-da68-4606-9e8d-8623c97a628f'"/>
    <el-table-column prop="name" label="Name" width="180" :data-testid="'1269c7fc-200c-4549-ba82-6a8782f441fa'"/>
    <el-table-column prop="address" label="Address" :data-testid="'89ad021f-c228-4321-a2ec-5c179a3c6171'"/>
  </el-table>
</template>

<script>
export default {
  data() {
    return {
      tableData: [
        { date: '2023-01-01', name: 'John', address: 'New York' },
        { date: '2023-01-02', name: 'Jane', address: 'London' },
        { date: '2023-01-03', name: 'Sam', address: 'Sydney' }
      ]
    }
  }
}
</script>
