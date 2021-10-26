<template>
	<a-layout>
		<a-layout-content>
			<div
				:class="{
					[$style.container]: true,
					cui__layout__squaredBorders: settings.isSquaredBorders,
					cui__layout__cardsShadow: settings.isCardShadow,
					cui__layout__borderless: settings.isBorderless,
					[$style.white]: settings.authPagesColor === 'white',
					[$style.gray]: settings.authPagesColor === 'gray',
				}"
				:style="{ backgroundImage: `url(resources/images/content/photos/7.jpg)` }"
			>
				<div :class="$style.containerInner">
					<transition :name="settings.routerAnimation" mode="out-in">
						<router-view />
					</transition>
				</div>
			</div>
		</a-layout-content>
	</a-layout>
</template>

<script>
import { mapState } from 'vuex'

export default {
	name: 'AuthLayout',
	computed: mapState(['settings']),
}
</script>

<style lang="scss" module>
@import './style.module.scss';
</style>
