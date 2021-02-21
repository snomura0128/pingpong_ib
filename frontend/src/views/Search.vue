<template>
  <v-container class="spacing-playground pa-6" fluid>
    <v-row>
      <v-col v-for="card in cards" :key="card.title" :cols="card.flex">
        <v-card>
          <v-img :src="card.src" class="white--text align-end" height="200px">
            <v-card-title v-text="card.title"></v-card-title>
          </v-img>

          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn icon>
              <v-icon>mdi-heart</v-icon>
            </v-btn>

            <v-btn icon>
              <v-icon>mdi-bookmark</v-icon>
            </v-btn>

            <v-btn icon>
              <v-icon>mdi-share-variant</v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col class="d-flex align-center" cols="12" sm="6">
        <v-text-field>
          <v-icon slot="append" color="red"> mdi-plus </v-icon>
          <v-icon slot="prepend" color="green"> mdi-minus </v-icon>
        </v-text-field>
      </v-col>
      <v-col class="d-flex align-center" cols="12" sm="6">
        <v-select :items="items" label="Outlined style" outlined></v-select>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    cards: [
      {
        title: "Pre-fab homes",
        src: "https://cdn.vuetifyjs.com/images/cards/house.jpg",
        flex: 12,
      },
      {
        title: "Favorite road trips",
        src: "https://cdn.vuetifyjs.com/images/cards/road.jpg",
        flex: 6,
      },
      {
        title: "Best airlines",
        src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg",
        flex: 6,
      },
    ],
    items: [
      { icon: "mdi-contacts", text: "search", path: "/search" },
      { icon: "mdi-history", text: "Frequently contacted", path: "/aaa" },
      { icon: "mdi-content-copy", text: "Duplicates", path: "/ccc" },
    ],
  }),
};
</script>
