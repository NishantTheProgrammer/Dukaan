<template>
  <div class="breadcrumb">
    <div class="container">
      <div class="breadcrumb-inner">
        <ul class="list-inline list-unstyled">
          <li><a href="#">Home</a></li>
          <li class="active">Handbags</li>
        </ul>
      </div>
      <!-- /.breadcrumb-inner -->
    </div>
    <!-- /.container -->
  </div>
  <!-- /.breadcrumb -->
  <div class="body-content outer-top-xs">
    <div class="container">
      <!-- ========================================== SECTION – HERO ========================================= -->


      <div class="search-result-container">
        <div id="myTabContent" class="tab-content category-list">
          <div class="tab-pane active" id="grid-container">
            <div class="category-product">
              <div class="row">
                <div
                  class="col-sm-4 col-md-3 col-lg-2"
                  v-for="product in categories"
                  :key="product.id"
                >
                  <div class="item">
                    <div class="products">
                      <div class="product">
                        <div class="product-image">
                          <div class="image">
                            <a href="detail.html">
                              <img :src="product.image" alt="" />
                              <!-- <img
                                    src="assets/images/products/p1_hover.jpg"
                                    alt=""
                                    class="hover-image"
                                  /> -->
                            </a>
                          </div>
                          <!-- /.image -->

                          <div class="tag new"><span>new</span></div>
                        </div>
                        <!-- /.product-image -->

                        <div class="product-info text-left">
                          <h3 class="name">
                            <a href="detail.html">{{ product.title }}</a>
                          </h3>
                          <div class="rating rateit-small"></div>
                          <div class="description"></div>
                          <!-- /.product-price -->
                        </div>
                        <!-- /.product-info -->
                        <div class="cart clearfix animate-effect">
                          <div class="action">
                            <ul class="list-unstyled">
                              <li class="add-cart-button btn-group">
                                <button
                                  class="btn btn-primary icon"
                                  data-toggle="dropdown"
                                  type="button"
                                >
                                  <i class="fa fa-shopping-cart"></i>
                                </button>
                                <button
                                  class="btn btn-primary cart-btn"
                                  type="button"
                                >
                                  Add to cart
                                </button>
                              </li>
                              <li class="lnk wishlist">
                                <a
                                  class="add-to-cart"
                                  href="detail.html"
                                  title="Wishlist"
                                >
                                  <i class="icon fa fa-heart"></i>
                                </a>
                              </li>
                              <li class="lnk">
                                <a
                                  class="add-to-cart"
                                  href="detail.html"
                                  title="Compare"
                                >
                                  <i class="fa fa-signal"></i>
                                </a>
                              </li>
                            </ul>
                          </div>
                          <!-- /.action -->
                        </div>
                        <!-- /.cart -->
                      </div>
                      <!-- /.product -->
                    </div>
                    <!-- /.products -->
                  </div>
                </div>
                <!-- /.item -->

                <!-- /.item -->
              </div>
              <!-- /.row -->
            </div>
            <!-- /.category-product -->
          </div>
          <!-- /.tab-pane -->

          <!-- /.tab-pane #list-container -->
        </div>
        <!-- /.tab-content -->
        <div class="clearfix filters-container bottom-row">
          <div class="text-right">
            <div class="pagination-container">
              <ul class="list-inline list-unstyled">
                <li class="prev">
                  <a href="#"><i class="fa fa-angle-left"></i></a>
                </li>
                <li><a href="#">1</a></li>
                <li class="active"><a href="#">2</a></li>
                <li><a href="#">3</a></li>
                <li><a href="#">4</a></li>
                <li class="next">
                  <a href="#"><i class="fa fa-angle-right"></i></a>
                </li>
              </ul>
              <!-- /.list-inline -->
            </div>
            <!-- /.pagination-container -->
          </div>
          <!-- /.text-right -->
        </div>
        <!-- /.filters-container -->
      </div>
      <!-- /.search-result-container -->
      <!-- /.row -->
      <!-- ============================================== BRANDS CAROUSEL ============================================== -->
      <div id="brands-carousel" class="logo-slider">
        <div class="logo-slider-inner">
          <div
            id="brand-slider"
            class="owl-carousel brand-slider custom-carousel owl-theme"
          >
            <div class="item m-t-15">
              <a href="#" class="image">
                <img
                  data-echo="assets/images/brands/brand1.png"
                  src="assets/images/blank.gif"
                  alt=""
                />
              </a>
            </div>
            <!--/.item-->

            <div class="item m-t-10">
              <a href="#" class="image">
                <img
                  data-echo="assets/images/brands/brand2.png"
                  src="assets/images/blank.gif"
                  alt=""
                />
              </a>
            </div>
            <!--/.item-->

            <div class="item">
              <a href="#" class="image">
                <img
                  data-echo="assets/images/brands/brand3.png"
                  src="assets/images/blank.gif"
                  alt=""
                />
              </a>
            </div>
            <!--/.item-->

            <div class="item">
              <a href="#" class="image">
                <img
                  data-echo="assets/images/brands/brand4.png"
                  src="assets/images/blank.gif"
                  alt=""
                />
              </a>
            </div>
            <!--/.item-->

            <div class="item">
              <a href="#" class="image">
                <img
                  data-echo="assets/images/brands/brand5.png"
                  src="assets/images/blank.gif"
                  alt=""
                />
              </a>
            </div>
            <!--/.item-->

            <div class="item">
              <a href="#" class="image">
                <img
                  data-echo="assets/images/brands/brand6.png"
                  src="assets/images/blank.gif"
                  alt=""
                />
              </a>
            </div>
            <!--/.item-->

            <div class="item">
              <a href="#" class="image">
                <img
                  data-echo="assets/images/brands/brand2.png"
                  src="assets/images/blank.gif"
                  alt=""
                />
              </a>
            </div>
            <!--/.item-->

            <div class="item">
              <a href="#" class="image">
                <img
                  data-echo="assets/images/brands/brand4.png"
                  src="assets/images/blank.gif"
                  alt=""
                />
              </a>
            </div>
            <!--/.item-->

            <div class="item">
              <a href="#" class="image">
                <img
                  data-echo="assets/images/brands/brand1.png"
                  src="assets/images/blank.gif"
                  alt=""
                />
              </a>
            </div>
            <!--/.item-->

            <div class="item">
              <a href="#" class="image">
                <img
                  data-echo="assets/images/brands/brand5.png"
                  src="assets/images/blank.gif"
                  alt=""
                />
              </a>
            </div>
            <!--/.item-->
          </div>
          <!-- /.owl-carousel #logo-slider -->
        </div>
        <!-- /.logo-slider-inner -->
      </div>
      <!-- /.logo-slider -->
      <!-- ============================================== BRANDS CAROUSEL : END ============================================== -->
    </div>
    <!-- /.container -->
  </div>
  <!-- /.body-content -->
  <!-- ============================================================= FOOTER ============================================================= -->

  <!-- ============================================== INFO BOXES ============================================== -->
  <div class="row our-features-box">
    <div class="container">
      <ul>
        <li>
          <div class="feature-box">
            <div class="icon-truck"></div>
            <div class="content-blocks">We ship worldwide</div>
          </div>
        </li>
        <li>
          <div class="feature-box">
            <div class="icon-support"></div>
            <div class="content-blocks">call +1 800 789 0000</div>
          </div>
        </li>
        <li>
          <div class="feature-box">
            <div class="icon-money"></div>
            <div class="content-blocks">Money Back Guarantee</div>
          </div>
        </li>
        <li>
          <div class="feature-box">
            <div class="icon-return"></div>
            <div class="content">30 days return</div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>


<script lang="ts">
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
import axios from "@/axios";
import { defineComponent } from "vue";

export default defineComponent({
  name: "Home",
  data() {
    return {
      categories: null as any,
    };
  },
  mounted() {
    axios.get("category/").then(({ data }: any) => {
      this.categories = data;
    });
  },
});
</script>
