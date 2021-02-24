<template>
  <v-container class="pa-1">
    <v-row>
      <v-col>
        <v-card class="pa-2">
          <v-card-title class="pa-1">検索条件</v-card-title>
          <v-row class="mt-0">
            <v-col>
              <v-expansion-panels v-model="wardPanelOpend">
                <v-expansion-panel>
                  <v-expansion-panel-header
                    class="pa-1"
                    disabled
                    style="cursor: default"
                    id="wardPanelHeader"
                  >
                    <template v-slot:actions>
                      <v-icon color="primary">mdi-chevron-triple-down</v-icon>
                    </template>
                    <v-chip class="ma-2" color="green" text-color="white">
                      地域
                    </v-chip>
                    <v-checkbox
                      v-model="isAllWardsSelected"
                      @click="selectAllWards"
                      hide-details
                      label="すべて"
                      class="mt-0"
                    ></v-checkbox
                  ></v-expansion-panel-header>
                  <v-expansion-panel-content>
                    <v-row>
                      <v-col
                        v-for="(wardpart, i) in [
                          wards.slice(0, 12),
                          wards.slice(12, 23),
                        ]"
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
                  </v-expansion-panel-content>
                </v-expansion-panel>
              </v-expansion-panels>
            </v-col>
          </v-row>

          <v-row class="mt-0">
            <v-col>
              <v-expansion-panels v-model="facilityTypePanelOpend">
                <v-expansion-panel>
                  <v-expansion-panel-header
                    class="pa-1"
                    disabled
                    style="cursor: default"
                    id="facilityTypePanelHeader"
                  >
                    <template v-slot:actions>
                      <v-icon color="primary">mdi-chevron-triple-down</v-icon>
                    </template>
                    <v-chip class="ma-2" color="green" text-color="white">
                      区分
                    </v-chip>
                    <v-checkbox
                      v-model="isAllFacilityTypesSelected"
                      @click="selectAllFacilityTypes"
                      hide-details
                      label="すべて"
                      class="mt-0"
                    ></v-checkbox>
                  </v-expansion-panel-header>
                  <v-expansion-panel-content>
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
                  </v-expansion-panel-content>
                </v-expansion-panel>
              </v-expansion-panels>
            </v-col>
          </v-row>

          <v-row class="mt-0">
            <v-col>
              <v-text-field
                solo
                hide-details
                prepend-inner-icon="mdi-magnify"
                label="キーワード検索"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row class="mt-0">
            <v-col>
              <v-btn elevation="4" block color="primary">検索</v-btn></v-col
            >
          </v-row>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col
        v-for="facility in response"
        v-bind:key="facility.id"
        cols="12"
        sm="6"
        md="4"
      >
        <v-card color="primary" class="spacing-playground py-2">
          <v-card-title class="font-weight-bold py-1 white--text">
            <VueResponsiveText>{{ facility.name }}</VueResponsiveText>
          </v-card-title>
          <v-card-text class="pa-2">
            <v-row align="center" class="mx-0">
              <v-rating
                :value="facility.evaluation"
                color="amber"
                dense
                half-increments
                readonly
                size="14"
              ></v-rating>
              <div class="white--text ml-4">
                {{ facility.evaluation }}
              </div>
            </v-row>
          </v-card-text>
          <v-card-text class="pa-1">
            <v-chip-group>
              <v-chip
                v-for="facilityType in facility.facilityTypes"
                v-bind:key="facilityType"
                :color="facilityTypes[facilityType - 1].color"
                label
                text-color="white"
                class="my-0"
              >
                <v-icon left small> mdi-label </v-icon>
                {{ facilityTypes[facilityType - 1].name }}
              </v-chip>
            </v-chip-group>
          </v-card-text>
          <v-card>
            <v-img
              :src="facility.imageUrl"
              height="125"
              contain
              class="grey darken-4"
            ></v-img>
          </v-card>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import $ from "jquery";
import VueResponsiveText from "vue-responsive-text";
export default {
  data: () => ({
    isAllWardsSelected: true,
    isAllFacilityTypesSelected: true,
    wardPanelOpend: null,
    facilityTypePanelOpend: null,
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
      { id: 1, name: "体育館", color: "red" },
      { id: 2, name: "卓球教室", color: "green" },
      { id: 3, name: "卓球バー", color: "yellow" },
      { id: 4, name: "卓球スタジオ", color: "black" },
      { id: 5, name: "その他", color: "pink" },
    ],
    selectedWardIds: [...Array(23)].map((_, i) => i + 1),
    selectedFacilityTypeIds: [...Array(5)].map((_, i) => i + 1),
    response: [
      {
        id: 1,
        name: "新宿区コズミックセンター",
        facilityTypes: [1],
        imageUrl:
          "https://www.regasu-shinjuku.or.jp/regasu/wp-content/uploads/2010/04/3e37f68e2bd1b9c7d00bd1aa7e5f7844-420x296.jpg",
        evaluation: 4.2,
      },
      {
        id: 2,
        name: "新宿スポーツセンター",
        facilityTypes: [1],
        imageUrl:
          "http://www.shinjuku-sportscenter.com/images/facility/facility_main_b.jpg",
        evaluation: 4.1,
      },
      {
        id: 3,
        name: "江戸川区グリーンパレス",
        facilityTypes: [1],
        imageUrl:
          "https://www.green-palace.jp/share/facility/img/facility_01.jpg",
        evaluation: 4.1,
      },
      {
        id: 4,
        name: "台東区リバーサイドスポーツセンター",
        facilityTypes: [1],
        imageUrl:
          "https://www.taitocity.net/zaidan/riverside/wp-content/uploads/sites/2/2015/12/river_top01.png",
        evaluation: 5.0,
      },
      {
        id: 5,
        name: "卓球空間FunTable",
        facilityTypes: [2, 4],
        imageUrl:
          "https://funtable.info/wp-content/uploads/2020/12/junior-bosyu.jpg",
        evaluation: 2.2,
      },
      {
        id: 6,
        name: "卓球酒場 ぽん蔵 高田馬場店",
        facilityTypes: [3],
        imageUrl: "http://ponzo.jp/img/photo_baba1.png",
        evaluation: 3.2,
      },
    ],
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
  mounted: function () {
    const wardIcon = $("#wardPanelHeader").children(
      ".v-expansion-panel-header__icon"
    );
    wardIcon[0].style.cursor = "pointer";
    wardIcon[0].onclick = () => {
      this.wardPanelOpend = this.wardPanelOpend == null ? 0 : null;
    };

    const facilityTypeIcon = $("#facilityTypePanelHeader").children(
      ".v-expansion-panel-header__icon"
    );
    facilityTypeIcon[0].style.cursor = "pointer";
    facilityTypeIcon[0].onclick = () => {
      this.facilityTypePanelOpend =
        this.facilityTypePanelOpend == null ? 0 : null;
    };
  },
  filters: {
    // fillSpace: function (value) {
    //   console.log(value.bytes());
    //   if (value.bytes() > 20) {
    //     return value;
    //   } else {
    //     console.log(value);
    //     return "   " + value + "   ";
    //   }
    // },
  },
  components: {
    VueResponsiveText,
  },
};
</script>
<style scoped>
.v-expansion-panel-header > *:not(.v-expansion-panel-header__icon) {
  flex: initial;
}
</style>
