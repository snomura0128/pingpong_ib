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
                      <v-checkbox
                        v-for="(ward, i) in wards"
                        v-bind:key="i"
                        v-bind:label="ward.name"
                        :value="ward.id"
                        v-model="selectedWardIds"
                        hide-details
                        class="ward-checkbox mt-0"
                        width="15px"
                      ></v-checkbox>
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
                      ジャンル
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
                      <v-checkbox
                        v-for="facilityType in facilityTypes"
                        v-bind:key="facilityType.id"
                        v-bind:label="facilityType.name"
                        :value="facilityType.id"
                        v-model="selectedFacilityTypeIds"
                        hide-details
                        class="facility-type-checkbox mt-0"
                      ></v-checkbox>
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
              <v-btn elevation="4" block color="primary" @click="search()"
                >検索</v-btn
              ></v-col
            >
          </v-row>
        </v-card>
      </v-col>
    </v-row>
    <v-row v-show="loading" justify="center">
      <v-progress-circular
        :size="70"
        :width="7"
        color="primary"
        indeterminate
      ></v-progress-circular>
    </v-row>
    <v-row>
      <v-col
        v-for="facility in response"
        v-bind:key="facility.id"
        cols="12"
        sm="6"
        xl="4"
      >
        <v-card
          class="spacing-playground pb-2"
          hover
          :to="{ name: '' }"
          :ripple="false"
        >
          <v-card>
            <v-img
              :src="facility.imageUrl"
              class="grey darken-4"
              aspect-ratio="1.5"
            >
            </v-img>
          </v-card>
          <v-row class="pa-5">
            <v-chip
              v-for="facilityType in facility.facilityTypes"
              v-bind:key="facilityType"
              :color="facilityTypes[facilityType - 1].color"
              label
              text-color="white"
              class="mr-1"
            >
              <v-icon left x-small> mdi-label </v-icon>
              {{ facilityTypes[facilityType - 1].name }}
            </v-chip>
          </v-row>
          <v-card-title class="py-0">
            <!-- <template v-if="facility.name.bytes() < 25"
              >{{ facility.name }}
            </template> -->
            <template v-if="true">{{ facility.name }} </template>
            <VueResponsiveText v-else>{{ facility.name }}</VueResponsiveText>
          </v-card-title>
          <v-row class="mx-4 py-2">
            <v-rating
              :value="facility.evaluation"
              color="amber"
              dense
              half-increments
              readonly
              size="16"
            ></v-rating>
            <div class="ml-2">
              {{ facility.evaluation }}
            </div>
          </v-row>
          <v-row> </v-row>
          <v-btn
            icon
            color="pink"
            absolute
            right
            top
            @click="switchFavorite(facility.id)"
          >
            <v-icon v-if="facility.favorite">mdi-heart</v-icon>
            <v-icon v-else>mdi-heart-outline</v-icon>
          </v-btn>
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
    wardPanelOpend: 0,
    facilityTypePanelOpend: 0,
    loading: false,
    wards: [
      { id: "01", name: "千代田区" },
      { id: "02", name: "中央区" },
      { id: "03", name: "港区" },
      { id: "04", name: "新宿区" },
      { id: "05", name: "文京区" },
      { id: "06", name: "台東区" },
      { id: "07", name: "墨田区" },
      { id: "08", name: "江東区" },
      { id: "09", name: "品川区" },
      { id: "10", name: "目黒区" },
      { id: "11", name: "大田区" },
      { id: "12", name: "世田谷区" },
      { id: "13", name: "渋谷区" },
      { id: "14", name: "中野区" },
      { id: "15", name: "杉並区" },
      { id: "16", name: "豊島区" },
      { id: "17", name: "北区" },
      { id: "18", name: "荒川区" },
      { id: "19", name: "板橋区" },
      { id: "20", name: "練馬区" },
      { id: "21", name: "足立区" },
      { id: "22", name: "葛飾区" },
      { id: "23", name: "江戸川区" },
    ],
    facilityTypes: [
      { id: 1, name: "体育館", color: "deep-purple darken-2" },
      { id: 2, name: "卓球教室", color: "teal darken-2" },
      { id: 3, name: "卓球バー", color: "blue darken-4" },
      { id: 4, name: "卓球スタジオ", color: "orange darken-4" },
      { id: 5, name: "その他", color: "grey darken-3" },
    ],
    selectedWardIds: [...Array(23)].map((_, i) =>
      (i + 1).toString().padStart(2, 0)
    ),
    selectedFacilityTypeIds: [...Array(5)].map((_, i) => i + 1),
    response: [],
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
    switchFavorite(id) {
      for (var facility of this.response) {
        if (facility.id == id) {
          facility.favorite = !facility.favorite;
        }
      }
    },
    search: function () {
      this.response = [];
      this.loading = true;
      this.axios
        .get("/api/search")
        .then((res) => {
          this.loading = false;
          this.response = res.data;
        })
        .catch((e) => {
          alert(e);
          this.loading = false;
        });
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
  components: {
    VueResponsiveText,
  },
};
</script>
<style scoped>
.v-expansion-panel-header > *:not(.v-expansion-panel-header__icon) {
  flex: initial;
}
.v-input--selection-controls.v-input {
  width: 135px;
}
.v-btn--absolute.v-btn--top {
  top: 6px;
}
.v-btn--absolute.v-btn--right {
  right: 6px;
}
</style>
