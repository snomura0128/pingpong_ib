<template>
  <v-container class="spacing-playground pa-2" fluid>
    <v-row>
      <v-col>
        <v-card class="spacing-playground pa-2">
          <v-card-title>検索条件</v-card-title>
          <v-divider> </v-divider>
          <v-checkbox
            v-model="isAllWardsSelected"
            @click="selectAllWards"
            hide-details
            label="すべて"
            class="mt-0"
          ></v-checkbox>
          <v-row>
            <v-col
              v-for="(wardpart, i) in [wards.slice(0, 12), wards.slice(12, 23)]"
              v-bind:key="i"
              cols="12"
              sm="6"
            >
              <v-row>
                <v-col
                  v-for="(wardTemp, j) in [
                    wardpart.slice(0, 6),
                    wardpart.slice(6),
                  ]"
                  v-bind:key="j"
                >
                  <v-checkbox
                    v-for="ward in wardTemp"
                    v-bind:key="ward.id"
                    v-bind:label="ward.name"
                    :value="ward.id"
                    v-model="selectedWardIds"
                    hide-details
                    class="ward-checkbox mt-0"
                  ></v-checkbox>
                </v-col>
              </v-row>
            </v-col>
          </v-row>
          <v-divider class="my-1"> </v-divider>
          <v-checkbox
            v-model="isAllFacilityTypesSelected"
            @click="selectAllFacilityTypes"
            hide-details
            label="すべて"
            class="mt-0"
          ></v-checkbox>
          <v-row>
            <v-col
              v-for="facilityType in facilityTypes"
              v-bind:key="facilityType.id"
            >
              <v-checkbox
                v-bind:label="facilityType.name"
                :value="facilityType.id"
                v-model="selectedFacilityTypeIds"
                hide-details
                class="facility-type-checkbox mt-0"
              ></v-checkbox>
            </v-col>
          </v-row>
          <v-divider class="my-1"> </v-divider>
          <v-row>
            <v-col class="my-1">
              <v-text-field
                flat
                solo-inverted
                hide-details
                prepend-inner-icon="mdi-magnify"
                label="キーワード検索"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col class="pt-0">
              <v-btn elevation="4" block color="primary">検索</v-btn></v-col
            >
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
22
<script>
export default {
  data: () => ({
    isAllWardsSelected: true,
    isAllFacilityTypesSelected: true,
    wards: [
      { id: 1, name: "足立区" },
      { id: 2, name: "荒川区" },
      { id: 3, name: "板橋区" },
      { id: 4, name: "江戸川区" },
      { id: 5, name: "大田区" },
      { id: 6, name: "葛飾区" },
      { id: 7, name: "北区" },
      { id: 8, name: "江東区" },
      { id: 9, name: "品川区" },
      { id: 10, name: "渋谷区" },
      { id: 11, name: "新宿区" },
      { id: 12, name: "杉並区" },
      { id: 13, name: "墨田区" },
      { id: 14, name: "世田谷区" },
      { id: 15, name: "台東区" },
      { id: 16, name: "千代田区" },
      { id: 17, name: "中央区" },
      { id: 18, name: "豊島区" },
      { id: 19, name: "中野区" },
      { id: 20, name: "練馬区" },
      { id: 21, name: "文京区" },
      { id: 22, name: "港区" },
      { id: 23, name: "目黒区" },
    ],
    facilityTypes: [
      { id: 1, name: "体育館" },
      { id: 2, name: "卓球教室" },
      { id: 3, name: "卓球バー" },
      { id: 4, name: "卓球スタジオ" },
      { id: 5, name: "その他" },
    ],
    selectedWardIds: [...Array(23)].map((_, i) => i + 1),
    selectedFacilityTypeIds: [...Array(5)].map((_, i) => i + 1),
  }),
  methods: {
    selectAllWards() {
      if (!this.isAllWardsSelected) {
        this.selectedWardIds = [];
        this.isAllWardsSelected = false;
      } else {
        this.selectedWardIds = [];
        for (var ward in this.wards) {
          this.selectedWardIds.push(this.wards[ward].id);
        }
        this.isAllWardsSelected = true;
      }
    },
    selectAllFacilityTypes() {
      if (!this.isAllFacilityTypesSelected) {
        this.selectedFacilityTypeIds = [];
        this.isAllFacilityTypesSelected = false;
      } else {
        this.selectedFacilityTypeIds = [];
        for (var facilityType in this.facilityTypes) {
          this.selectedFacilityTypeIds.push(
            this.facilityTypes[facilityType].id
          );
        }
        this.isAllFacilityTypesSelected = true;
      }
    },
  },
};
</script>
