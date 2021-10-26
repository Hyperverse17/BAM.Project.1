import Vue from 'vue'
import Router from 'vue-router'
import AuthLayout from '@/layouts/Auth'
import MainLayout from '@/layouts/Main'
import store from '@/store'

Vue.use(Router)

const router = new Router({
	base: process.env.BASE_URL,
	scrollBehavior() {
		return { x: 0, y: 0 }
	},
	routes: [
		{
			path: '/',
			redirect: 'customers',
			component: MainLayout,
			meta: {
				authRequired: true,
				hidden: true,
			},
			children: [
				// Clients
				{
					path: '/customers',
					meta: {
						title: 'Clientes',
					},
					component: () => import('./views/customers'),
				},
				{
					path: '/customers/:id',
					meta: {
						title: 'Clientes - Detalle',
					},
					component: () => import('./views/customers/details'),
				},
			],
		},

		// System Pages
		{
			path: '/auth',
			component: AuthLayout,
			redirect: 'auth/login',
			children: [
				{
					path: '/auth/404',
					meta: {
						title: 'Error',
					},
					component: () => import('./views/auth/404'),
				},

				{
					path: '/auth/login',
					meta: {
						title: 'Inicio de sesión',
					},
					component: () => import('./views/auth/login'),
				},
			],
		},

		// Redirect to 404
		{
			path: '*',
			redirect: 'auth/404',
			hidden: true,
		},
	],
})

router.beforeEach((to, from, next) => {
	if (to.matched.some((record) => record.meta.authRequired)) {
		if (!store.state.user.authorized) {
			next({
				path: '/auth/login',
				query: { redirect: to.fullPath },
			})
		} else {
			next()
		}
	} else {
		next()
	}
})

export default router
