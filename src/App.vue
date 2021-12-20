<template>
  <Header />
  <router-view/>
  <Footer />
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Header from "@/components/Header.vue"; // @ is an alias to /src
import Footer from "@/components/Footer.vue"; // @ is an alias to /src
export default defineComponent({
  name: "Terms",
  components: {
    Header,
    Footer,
  },
});
</script>


