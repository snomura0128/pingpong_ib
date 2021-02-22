<template>
  <v-container class="spacing-playground pa-6" fluid>
    <v-row>
      <v-col>
        <v-card>
          <v-img
            src="https://cdn.vuetifyjs.com/images/cards/house.jpg"
            class="white--text align-end"
            height="200px"
          >
            <v-card-title></v-card-title>
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
      <v-col
        v-for="(wardpart, i) in [
          wards.slice(0, 4),
          wards.slice(4, 8),
          wards.slice(8, 12),
          wards.slice(12, 16),
          wards.slice(16, 20),
          wards.slice(20, 23),
        ]"
        v-bind:key="i"
        cols="12"
        sm="2"
        md="2"
      >
        <v-checkbox
          v-for="ward in wardpart"
          v-bind:key="ward.value"
          v-bind:label="ward.text"
          v-bind:id="ward.key"
          hide-details
          value="true"
        ></v-checkbox>
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
        <v-select label="Outlined style" outlined></v-select>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    wards: [
      { value: 1, text: "足立区" },
      { value: 2, text: "荒川区" },
      { value: 3, text: "板橋区" },
      { value: 4, text: "江戸川区" },
      { value: 5, text: "大田区" },
      { value: 6, text: "葛飾区" },
      { value: 7, text: "北区" },
      { value: 8, text: "江東区" },
      { value: 9, text: "品川区" },
      { value: 10, text: "渋谷区" },
      { value: 11, text: "新宿区" },
      { value: 12, text: "杉並区" },
      { value: 13, text: "墨田区" },
      { value: 14, text: "世田谷区" },
      { value: 15, text: "台東区" },
      { value: 16, text: "千代田区" },
      { value: 17, text: "中央区" },
      { value: 18, text: "豊島区" },
      { value: 19, text: "中野区" },
      { value: 20, text: "練馬区" },
      { value: 21, text: "文京区" },
      { value: 22, text: "港区" },
      { value: 23, text: "目黒区" },
    ],
  }),
};
</script>

<style scoped>
.v-input--selection-controls {
  margin-top: 0;
}
</style>
