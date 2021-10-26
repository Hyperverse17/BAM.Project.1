/* eslint-disable no-console */
console.log('********* SERVICE WORKER REGISTRATION ********')
import { register } from 'register-service-worker'
import Swal from 'sweetalert2'

if (process.env.NODE_ENV === 'production') {
	register(`${process.env.BASE_URL}service-worker.js`, {
		registrationOptions: {
			scope: process.env.BASE_URL,
		},
		ready() {
			console.log('App is being served from cache by a service worker.\n' + 'For more details, visit https://goo.gl/AFskqB')
		},
		registered() {
			console.log('Service worker has been registered.')
		},
		cached() {
			console.log('Content has been cached for offline use.')
			Swal.hideLoading()
			Swal.close()
			location.reload()
		},
		updatefound() {
			console.log('New content is downloading.')
			localStorage.clear()
			Swal.fire({
				title: 'Espera un momento por favor',
				text: 'Estamos actualizando a la última versión de nuestro sistema. Esto no tardará demasiado.',
				timer: 5 * 60 * 1000,
				showCancelButton: false,
				showCloseButton: false,
				showConfirmButton: false,
				allowEscapeKey: false,
				allowEnterKey: false,
				allowOutsideClick: false,
				backdrop: true,
				onBeforeOpen: () => {
					Swal.showLoading()
				},
			})
		},
		updated() {
			console.log('New content is available; please refresh.')
			Swal.hideLoading()
			Swal.close()
			location.reload()
		},
		offline() {
			console.log('No internet connection found. App is running in offline mode.')
		},
		error(error) {
			console.error('Error during service worker registration:', error)
		},
	})
}
