<template>
	<div>
		<div class="card" :class="$style.container">
			<div class="text-dark font-size-24 mb-3">
				<strong>Ingreso a sistema</strong>
			</div>
			<a-form class="mb-4" :form="form" @submit="handleSubmit">
				<a-form-item label="Email">
					<a-input
						size="large"
						placeholder="Email"
						v-decorator="[
							'email',
							{
								rules: [
									{
										required: true,
										message: 'Ingresa email válido',
									},
								],
							},
						]"
					/>
				</a-form-item>
				<a-form-item label="Contraseña">
					<a-input
						size="large"
						placeholder="Password"
						type="password"
						v-decorator="[
							'password',
							{
								rules: [
									{
										required: true,
										message: 'Ingresa tu contraseña',
									},
								],
							},
						]"
					/>
				</a-form-item>
				<a-button type="primary" htmlType="submit" size="large" class="text-center w-100" :loading="loading">
					<strong>Ingresar</strong>
				</a-button>
			</a-form>
		</div>
	</div>
</template>
<script>
import { mapState } from 'vuex'

export default {
	name: 'CuiLogin',
	computed: {
		...mapState(['settings']),
		loading() {
			return this.$store.state.user.loading
		},
	},
	data: function () {
		return {
			form: this.$form.createForm(this),
		}
	},
	methods: {
		changeAuthProvider(value) {
			this.$store.commit('CHANGE_SETTING', { setting: 'authProvider', value })
		},
		handleSubmit(e) {
			e.preventDefault()
			this.form.validateFields((err, values) => {
				if (!err) {
					this.$store.dispatch('user/LOGIN', { payload: values })
				}
			})
		},
	},
}
</script>
<style lang="scss" module>
@import '@/components/cleanui/system/Auth/style.module.scss';
</style>
