
import streamlit as st

st.set_page_config(page_title="Quảng Cáo Sản Phẩm Đơn Giản", layout="centered")

st.title("🛒 Quảng Cáo Sản Phẩm Đơn Giản")
st.write("Chào anh! Đây là nơi để anh đăng sản phẩm và cho người khác xem.")

st.header("📸 Đăng sản phẩm mới")
uploaded_images = st.file_uploader("Tải hình sản phẩm (tối đa 3)", accept_multiple_files=True, type=["jpg", "jpeg", "png"])
product_name = st.text_input("Tên sản phẩm")
product_desc = st.text_area("Mô tả ngắn")
product_price = st.number_input("Giá bán (USD)", min_value=0.0, format="%.2f")

if st.button("✅ Đăng sản phẩm"):
    st.success("Đăng sản phẩm thành công!")
    st.write("### Thông tin sản phẩm:")
    st.write(f"**Tên:** {product_name}")
    st.write(f"**Mô tả:** {product_desc}")
    st.write(f"**Giá bán:** ${product_price:.2f}")
    if uploaded_images:
        st.write("**Hình ảnh:**")
        for img in uploaded_images:
            st.image(img, width=200)
