<template>
	<div>
		<h1>Prospectos de clientes</h1>
		<a-table :columns="columns" :data-source="data">
			<a slot="name" slot-scope="text">{{ text }}</a>
			<span slot="tags" slot-scope="tags">
				<a-tag v-for="tag in tags" :key="tag" :color="tag === 'Rechazado' ? 'volcano' : tag.length > 5 ? 'geekblue' : 'green'">
					{{ tag.toUpperCase() }}
				</a-tag>
			</span>
			<span slot="action" slot-scope="record">
				<a-button @click="edit(record.key)" icon="edit" />
			</span>
		</a-table>
	</div>
</template>

<script>
const columns = [
	{
		title: 'Nombre',
		dataIndex: 'name',
		key: 'name',
	},
	{
		title: 'Fecha de nacimiento',
		dataIndex: 'birthdate',
		key: 'birthdate',
	},
	{
		title: 'Correo',
		dataIndex: 'email',
		key: 'email',
	},
	{
		title: 'Estatus',
		key: 'tags',
		dataIndex: 'tags',
		scopedSlots: { customRender: 'tags' },
	},
	{
		title: 'Acción',
		key: 'action',
		scopedSlots: { customRender: 'action' },
	},
]

const data = [
	{
		key: '1',
		name: 'John Brown',
		birthdate: '1991/09/01',
		email: 'brown@mail.com',
		tags: ['Nuevo'],
	},
	{
		key: '2',
		name: 'Jim Green',
		birthdate: '1987/12/11',
		email: 'green_jim_1987@the-mail.com',
		tags: ['Rechazado'],
	},
	{
		key: '3',
		name: 'Joe Black',
		birthdate: '2000/01/01',
		email: 'the-black-joe@newmail.com',
		tags: ['Atendido'],
	},
]

export default {
	data() {
		return {
			data,
			columns,
		}
	},
	methods: {
		edit(id) {
			this.$router.push(`/customers/${id}`)
		},
	},
}
</script>