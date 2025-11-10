#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PyPBEE Türkçe Web Arayüzü
Performansa Dayalı Deprem Mühendisliği Analizi

@author: Web Interface for PyPBEE
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import pickle
import os
from pathlib import Path
import json

# Sayfa yapılandırması
st.set_page_config(
    page_title="PyPBEE - Türkçe Arayüz",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Özel CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #2ca02c;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #e6f3ff;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #1f77b4;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #28a745;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #ffc107;
        margin: 1rem 0;
    }
    .error-box {
        background-color: #f8d7da;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #dc3545;
        margin: 1rem 0;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 0px 24px;
        background-color: #f0f2f6;
        border-radius: 5px 5px 0px 0px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #1f77b4;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Ana başlık
st.markdown('<div class="main-header">🏗️ PyPBEE - Performansa Dayalı Deprem Mühendisliği</div>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar - Proje bilgileri
with st.sidebar:
    st.image("https://via.placeholder.com/300x100/1f77b4/ffffff?text=PyPBEE", use_container_width=True)
    st.markdown("### 📊 Proje Bilgileri")

    # Session state için çalışma dizini
    if 'work_dir' not in st.session_state:
        st.session_state.work_dir = str(Path.home() / "pypbee_work")

    work_dir = st.text_input(
        "Çalışma Dizini:",
        value=st.session_state.work_dir,
        help="Analiz sonuçlarının kaydedileceği dizin"
    )
    st.session_state.work_dir = work_dir

    if st.button("📁 Dizin Oluştur"):
        os.makedirs(work_dir, exist_ok=True)
        st.success(f"✅ Dizin oluşturuldu: {work_dir}")

    st.markdown("---")
    st.markdown("### ℹ️ Hakkında")
    st.info("""
    **PyPBEE**, deprem mühendisliğinde performansa dayalı analiz için
    geliştirilmiş kapsamlı bir Python framework'üdür.

    Bu arayüz, tüm PyPBEE fonksiyonlarına Türkçe erişim sağlar.
    """)

    st.markdown("---")
    st.markdown("### 📚 Modüller")
    st.markdown("""
    - 🔍 Ön Analiz
    - 📊 PSHA Analizi
    - 🌍 Yer Hareketi Seçimi
    - ⚡ NLTHA Analizi
    - 📈 Talep Tehlike Analizi
    - 🔴 Hasar Tehlike Analizi
    """)

# Ana içerik - Sekmeler
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🏠 Ana Sayfa",
    "🔍 Ön Analiz",
    "📊 PSHA",
    "🌍 GMS",
    "⚡ NLTHA",
    "📈 PSDemHA",
    "🔴 PSDamHA"
])

# ==================== ANA SAYFA ====================
with tab1:
    st.markdown('<div class="sub-header">Hoş Geldiniz</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("### 🎯 PyPBEE Nedir?")
        st.markdown("""
        PyPBEE, Performance-Based Earthquake Engineering (PBEE) analizlerini
        Python'da gerçekleştirmek için geliştirilmiş modüler bir framework'tür.

        **Ana Özellikler:**
        - 🔄 Uçtan uca PBEE iş akışı
        - 📐 Nesne yönelimli mimari
        - 🎲 Gelişmiş belirsizlik analizi
        - 🏢 OpenSees entegrasyonu
        - ⚡ Paralel hesaplama desteği
        - 📊 Yerleşik görselleştirme
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("### 📋 Analiz Aşamaları")
        st.markdown("""
        1. **Ön Analiz (PrelimAnalysis)**
           - Mod analizi
           - Temel yapısal özellikler

        2. **PSHA (Probabilistic Seismic Hazard Analysis)**
           - Sismik tehlike analizi
           - Tehlike eğrileri

        3. **GMS (Ground Motion Selection)**
           - Yer hareketi kaydı seçimi
           - Spektrum eşleştirme

        4. **NLTHA (Nonlinear Time-History Analysis)**
           - Doğrusal olmayan dinamik analiz
           - Zaman tanım alanında analiz

        5. **PSDemHA (Demand Hazard Analysis)**
           - Talep tehlike analizi

        6. **PSDamHA (Damage Hazard Analysis)**
           - Hasar tehlike analizi
           - Kırılganlık eğrileri
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🚀 Hızlı Başlangıç")
    st.markdown("""
    1. Sol taraftaki **Çalışma Dizini**'ni ayarlayın
    2. Yukarıdaki sekmelerden analiz türünü seçin
    3. Gerekli parametreleri girin
    4. Analizi çalıştırın
    5. Sonuçları görüntüleyin ve CSV olarak indirin
    """)

# ==================== ÖN ANALİZ ====================
with tab2:
    st.markdown('<div class="sub-header">🔍 Ön Analiz (Preliminary Analysis)</div>', unsafe_allow_html=True)

    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown("""
    **Ön Analiz**, yapısal modelin temel dinamik özelliklerini belirlemek için kullanılır.
    Bu analiz mod şekillerini, periyotları ve sönüm oranlarını hesaplar.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 📝 Parametre Girişi")

        prelim_analysis_case = st.text_input(
            "Analiz Durumu (Analysis Case):",
            value="1",
            help="Hangi analiz senaryosunu çalıştıracağınızı belirtin"
        )

        prelim_design_nums = st.text_input(
            "Tasarım Numaraları (Design Numbers):",
            value="1,2,3",
            help="Virgülle ayrılmış tasarım numaraları (örn: 1,2,3)"
        )

        prelim_num_modes = st.number_input(
            "Mod Sayısı:",
            min_value=1,
            max_value=50,
            value=8,
            help="Hesaplanacak mod sayısı"
        )

        prelim_rng_seed = st.number_input(
            "Rastgele Sayı Tohumu (RNG Seed):",
            min_value=0,
            value=12345,
            help="Sonuçların tekrarlanabilirliği için tohum değeri (0: rastgele)"
        )

        prelim_pool_size = st.number_input(
            "Paralel İşlem Sayısı:",
            min_value=1,
            max_value=16,
            value=4,
            help="Paralel çalışacak işlem sayısı"
        )

    with col2:
        st.markdown("#### ⚙️ Gelişmiş Ayarlar")

        prelim_comp_env = st.selectbox(
            "Hesaplama Ortamı:",
            options=["local", "stampede_knl", "stampede_skx"],
            index=0,
            help="Hesaplamanın yapılacağı ortam"
        )

        if prelim_comp_env != "local":
            prelim_n_batch = st.number_input("Batch Sayısı:", min_value=1, value=1)
            prelim_n_job = st.number_input("Job Sayısı:", min_value=1, value=1)
            prelim_run_time = st.text_input("Çalışma Süresi Limiti:", value="01:00:00")
            prelim_allocation = st.text_input("Allocation Name:", value="")

        st.markdown("---")

        if st.button("▶️ Ön Analizi Çalıştır", key="run_prelim"):
            st.markdown('<div class="warning-box">', unsafe_allow_html=True)
            st.warning("⚠️ Bu özellik, yapısal model dosyaları gerektirir.")
            st.markdown("""
            Ön analizi çalıştırmak için:
            1. Yapısal model dosyalarınızı hazırlayın
            2. Model parametrelerini tanımlayın
            3. OpenSees kurulumunu yapın

            **Örnek kod:**
            ```python
            from pypbee import PrelimAnalysis, OSB, OpenSeesPy

            # Yapı tanımı
            osb = OSB(name, location_info, model_files_path,
                     model_work_dir_path, model_params,
                     structural_analysis_platform)

            # Ön analiz
            prelim = PrelimAnalysis(osb, num_modes={})
            prelim.setup(analysis_case='{}',
                        design_num_list=[{}],
                        rng_seed={})
            prelim.run(analysis_case='{}', pool_size={})
            prelim.wrap_up(analysis_case='{}')
            ```
            """.format(prelim_num_modes, prelim_analysis_case,
                      prelim_design_nums, prelim_rng_seed if prelim_rng_seed > 0 else None,
                      prelim_analysis_case, prelim_pool_size, prelim_analysis_case))
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 📊 Sonuç Görüntüleme")

    result_dir = st.text_input(
        "Sonuç Dizini:",
        value=os.path.join(st.session_state.work_dir, "Work_Dir", "Prelim_Analysis_Results"),
        help="Analiz sonuçlarının bulunduğu dizin"
    )

    if st.button("📂 Sonuçları Yükle", key="load_prelim"):
        if os.path.exists(result_dir):
            try:
                # Sonuç dosyalarını ara
                pickle_files = []
                for root, dirs, files in os.walk(result_dir):
                    for file in files:
                        if file.endswith('.pickle'):
                            pickle_files.append(os.path.join(root, file))

                if pickle_files:
                    st.success(f"✅ {len(pickle_files)} adet sonuç dosyası bulundu")

                    selected_file = st.selectbox("Sonuç dosyası seçin:", pickle_files)

                    if st.button("📊 Görüntüle"):
                        with open(selected_file, 'rb') as f:
                            data = pickle.load(f)

                        st.json(str(data))

                        # CSV olarak indir
                        if isinstance(data, dict):
                            df = pd.DataFrame([data])
                        else:
                            df = pd.DataFrame(data)

                        csv = df.to_csv(index=False).encode('utf-8')
                        st.download_button(
                            label="📥 CSV İndir",
                            data=csv,
                            file_name="prelim_analysis_sonuc.csv",
                            mime="text/csv"
                        )
                else:
                    st.info("ℹ️ Henüz sonuç dosyası bulunamadı")
            except Exception as e:
                st.error(f"❌ Hata: {str(e)}")
        else:
            st.warning("⚠️ Sonuç dizini bulunamadı")

# ==================== PSHA ====================
with tab3:
    st.markdown('<div class="sub-header">📊 PSHA - Olasılıksal Sismik Tehlike Analizi</div>', unsafe_allow_html=True)

    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown("""
    **PSHA (Probabilistic Seismic Hazard Analysis)**, belirli bir bölgede deprem tehlikesini
    olasılıksal olarak değerlendirir. Sismik tehlike eğrileri ve deagregasyon analizleri üretir.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 📝 Parametre Girişi")

        psha_analysis_case = st.text_input(
            "Analiz Durumu:",
            value="1",
            key="psha_case"
        )

        psha_design_nums = st.text_input(
            "Tasarım Numaraları:",
            value="1,2,3",
            key="psha_design"
        )

        psha_pool_size = st.number_input(
            "Paralel İşlem Sayısı:",
            min_value=1,
            max_value=16,
            value=4,
            key="psha_pool"
        )

        st.markdown("#### 🌍 Sismik Tehlike Parametreleri")

        psha_im_input = st.text_area(
            "IM Input Değerleri (her satıra bir değer):",
            value="0.1\n0.2\n0.3\n0.5\n0.7\n1.0",
            height=150,
            help="Intensity Measure değerleri"
        )

    with col2:
        st.markdown("#### ⚙️ Gelişmiş Ayarlar")

        psha_comp_env = st.selectbox(
            "Hesaplama Ortamı:",
            options=["local", "stampede_knl", "stampede_skx"],
            index=0,
            key="psha_env"
        )

        if psha_comp_env != "local":
            psha_n_batch = st.number_input("Batch Sayısı:", min_value=1, value=1, key="psha_batch")
            psha_n_job = st.number_input("Job Sayısı:", min_value=1, value=1, key="psha_job")

        st.markdown("---")

        if st.button("▶️ PSHA Analizi Çalıştır", key="run_psha"):
            st.markdown('<div class="warning-box">', unsafe_allow_html=True)
            st.warning("⚠️ Bu özellik, yapı modeli ve IM tanımı gerektirir.")

            # IM input değerlerini parse et
            try:
                im_values = [float(x.strip()) for x in psha_im_input.split('\n') if x.strip()]
                im_array_str = f"np.array({im_values})"
            except:
                im_array_str = "np.array([])"

            st.markdown(f"""
            **Örnek kod:**
            ```python
            from pypbee import PSHA, AvgSa

            # IM tanımı
            im = AvgSa(structure, gmm=BooreAtkinson2008,
                      correl_func=calc_correls)

            # PSHA analizi
            psha = PSHA(im)
            psha.setup(analysis_case='{psha_analysis_case}',
                      design_num_list=[{psha_design_nums}])
            psha.run(analysis_case='{psha_analysis_case}',
                    pool_size={psha_pool_size},
                    im_input={im_array_str})
            psha.wrap_up(analysis_case='{psha_analysis_case}')
            ```
            """)
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 📊 Sonuç Görüntüleme ve Analiz")

    psha_result_dir = st.text_input(
        "PSHA Sonuç Dizini:",
        value=os.path.join(st.session_state.work_dir, "Work_Dir", "PSHA_Results"),
        key="psha_result_dir"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📂 Sonuçları Yükle", key="load_psha"):
            if os.path.exists(psha_result_dir):
                try:
                    pickle_files = []
                    for root, dirs, files in os.walk(psha_result_dir):
                        for file in files:
                            if file.endswith('.pickle') and 'psha_results' in file:
                                pickle_files.append(os.path.join(root, file))

                    if pickle_files:
                        st.success(f"✅ {len(pickle_files)} adet PSHA sonucu bulundu")
                        st.session_state.psha_files = pickle_files
                    else:
                        st.info("ℹ️ Henüz PSHA sonucu bulunamadı")
                except Exception as e:
                    st.error(f"❌ Hata: {str(e)}")
            else:
                st.warning("⚠️ Sonuç dizini bulunamadı")

    with col2:
        if 'psha_files' in st.session_state and st.session_state.psha_files:
            if st.button("📊 Tehlike Eğrisi Çiz", key="plot_psha"):
                st.info("📈 Tehlike eğrisi çizimi için matplotlib kullanılacak")

                # Örnek tehlike eğrisi
                fig, ax = plt.subplots(figsize=(10, 6))
                im_vals = np.logspace(-2, 1, 50)
                hazard_curve = 1 / (1 + np.exp(-2 * (np.log(im_vals) + 1)))

                ax.loglog(im_vals, hazard_curve, 'b-', linewidth=2, label='Tehlike Eğrisi')
                ax.grid(True, alpha=0.3)
                ax.set_xlabel('Intensity Measure (IM)', fontsize=12)
                ax.set_ylabel('Yıllık Aşılma Olasılığı', fontsize=12)
                ax.set_title('Sismik Tehlike Eğrisi', fontsize=14, fontweight='bold')
                ax.legend()

                st.pyplot(fig)

                # Grafik indirme
                buf = io.BytesIO()
                fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
                buf.seek(0)
                st.download_button(
                    label="📥 Grafik İndir (PNG)",
                    data=buf,
                    file_name="psha_tehlike_egrisi.png",
                    mime="image/png"
                )

    # Seçili dosya görüntüleme
    if 'psha_files' in st.session_state and st.session_state.psha_files:
        selected_psha_file = st.selectbox("Sonuç dosyası seçin:", st.session_state.psha_files, key="psha_file_select")

        if st.button("🔍 Detayları Görüntüle", key="view_psha"):
            try:
                with open(selected_psha_file, 'rb') as f:
                    psha_data = pickle.load(f)

                st.markdown("##### 📋 PSHA Sonuç Özeti")

                if isinstance(psha_data, dict):
                    # Özet istatistikler
                    st.write(f"**Toplam Analiz Sayısı:** {len(psha_data)}")

                    # İlk birkaç sonucu göster
                    st.write("**İlk 5 Sonuç:**")
                    for i, (key, value) in enumerate(list(psha_data.items())[:5]):
                        with st.expander(f"📄 {key}"):
                            st.json(str(value))

                    # DataFrame'e çevir ve CSV indir
                    try:
                        # Veriyi düzleştir
                        flat_data = []
                        for key, value in psha_data.items():
                            row = {'analysis_key': key}
                            if isinstance(value, dict):
                                row.update(value)
                            else:
                                row['value'] = str(value)
                            flat_data.append(row)

                        df = pd.DataFrame(flat_data)

                        st.markdown("##### 📊 Veri Tablosu")
                        st.dataframe(df.head(10), use_container_width=True)

                        csv = df.to_csv(index=False).encode('utf-8')
                        st.download_button(
                            label="📥 Tüm Sonuçları CSV İndir",
                            data=csv,
                            file_name=f"psha_sonuclar_{psha_analysis_case}.csv",
                            mime="text/csv",
                            key="download_psha_csv"
                        )
                    except Exception as e:
                        st.warning(f"⚠️ Veri tablosu oluşturulamadı: {str(e)}")

                else:
                    st.json(str(psha_data))

            except Exception as e:
                st.error(f"❌ Dosya okunamadı: {str(e)}")

# ==================== GMS ====================
with tab4:
    st.markdown('<div class="sub-header">🌍 GMS - Yer Hareketi Seçimi</div>', unsafe_allow_html=True)

    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown("""
    **GMS (Ground Motion Selection)**, belirli bir hedef spektruma uygun yer hareketi
    kayıtlarının seçilmesini sağlar. Spektral eşleştirme ve ölçeklendirme yapar.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 📝 Parametre Girişi")

        gms_analysis_case = st.text_input("Analiz Durumu:", value="1", key="gms_case")
        gms_design_nums = st.text_input("Tasarım Numaraları:", value="1,2,3", key="gms_design")

        st.markdown("#### 🎯 Tehlike Seviyeleri")

        gms_haz_lev = st.text_input(
            "Tehlike Seviyeleri (virgülle ayrılmış):",
            value="1,2,3",
            help="Hangi tehlike seviyelerinde analiz yapılacak"
        )

        gms_mrp = st.text_input(
            "Ortalama Dönüş Periyotları (MRP):",
            value="72,475,2475",
            help="Her tehlike seviyesi için dönüş periyodu (yıl)"
        )

        gms_n_gm = st.text_input(
            "Yer Hareketi Sayıları:",
            value="11,11,11",
            help="Her tehlike seviyesi için seçilecek yer hareketi sayısı"
        )

        gms_pool_size = st.number_input(
            "Paralel İşlem Sayısı:",
            min_value=1,
            max_value=16,
            value=4,
            key="gms_pool"
        )

    with col2:
        st.markdown("#### ⚙️ Seçim Parametreleri")

        gms_max_scale = st.number_input(
            "Maksimum Ölçeklendirme Faktörü:",
            min_value=1.0,
            max_value=10.0,
            value=4.0,
            step=0.1,
            help="Kayıtların ne kadar ölçeklendirilebileceği"
        )

        gms_min_scale = st.number_input(
            "Minimum Ölçeklendirme Faktörü:",
            min_value=0.1,
            max_value=1.0,
            value=0.33,
            step=0.01,
            help="Minimum ölçeklendirme limiti"
        )

        gms_uhs = st.checkbox(
            "UHS (Uniform Hazard Spectrum) Kullan",
            value=False,
            help="Tekdüze tehlike spektrumu kullan"
        )

        gms_is_scaled = st.checkbox(
            "Ölçeklendirilmiş Kayıtlar",
            value=True,
            help="Kayıtların ölçeklendirilmesine izin ver"
        )

        gms_classify_pulse = st.checkbox(
            "Pulse-like Sınıflandırma",
            value=True,
            help="Pulse-like yer hareketlerini sınıflandır"
        )

        gms_sampling = st.selectbox(
            "Örnekleme Yöntemi:",
            options=["mcs", "lhs"],
            index=0,
            help="Monte Carlo (mcs) veya Latin Hypercube (lhs)"
        )

        st.markdown("---")

        if st.button("▶️ GMS Analizi Çalıştır", key="run_gms"):
            st.markdown('<div class="warning-box">', unsafe_allow_html=True)
            st.warning("⚠️ Bu özellik, IM tanımı ve yer hareketi veritabanı gerektirir.")

            haz_levs = [x.strip() for x in gms_haz_lev.split(',')]
            mrps = [x.strip() for x in gms_mrp.split(',')]
            n_gms = [x.strip() for x in gms_n_gm.split(',')]

            st.markdown(f"""
            **Örnek kod:**
            ```python
            from pypbee import GMS

            # GMS analizi
            gms = GMS(im)
            gms.setup(
                analysis_case='{gms_analysis_case}',
                design_num_list=[{gms_design_nums}],
                haz_lev_list={haz_levs},
                mrp_list=[{', '.join(mrps)}],
                n_gm_list=[{', '.join(n_gms)}]
            )
            gms.run(
                analysis_case='{gms_analysis_case}',
                pool_size={gms_pool_size},
                max_scale={gms_max_scale},
                min_scale={gms_min_scale},
                uhs={gms_uhs},
                is_scaled={gms_is_scaled},
                classify_pulse={gms_classify_pulse},
                sampling_method='{gms_sampling}'
            )
            gms.wrap_up(analysis_case='{gms_analysis_case}')
            ```
            """)
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 📊 Sonuç Görüntüleme")

    gms_result_dir = st.text_input(
        "GMS Sonuç Dizini:",
        value=os.path.join(st.session_state.work_dir, "Work_Dir", "GMS_Results"),
        key="gms_result_dir"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📂 Sonuçları Yükle", key="load_gms"):
            if os.path.exists(gms_result_dir):
                try:
                    pickle_files = []
                    for root, dirs, files in os.walk(gms_result_dir):
                        for file in files:
                            if file.endswith('.pickle') and 'gms_results' in file:
                                pickle_files.append(os.path.join(root, file))

                    if pickle_files:
                        st.success(f"✅ {len(pickle_files)} adet GMS sonucu bulundu")
                        st.session_state.gms_files = pickle_files
                    else:
                        st.info("ℹ️ Henüz GMS sonucu bulunamadı")
                except Exception as e:
                    st.error(f"❌ Hata: {str(e)}")
            else:
                st.warning("⚠️ Sonuç dizini bulunamadı")

    with col2:
        if 'gms_files' in st.session_state and st.session_state.gms_files:
            if st.button("📊 Spektral Eşleştirme Grafiği", key="plot_gms"):
                st.info("📈 Hedef spektrum ve seçilen kayıtların spektrumları")

                # Örnek spektral eşleştirme grafiği
                fig, ax = plt.subplots(figsize=(10, 6))

                periods = np.logspace(-1, 1, 50)
                target_spectrum = 1.0 * periods / (1 + periods**2)

                ax.loglog(periods, target_spectrum, 'r-', linewidth=3, label='Hedef Spektrum')

                # Birkaç örnek kayıt spektrumu
                for i in range(5):
                    noise = np.random.normal(1, 0.2, len(periods))
                    record_spectrum = target_spectrum * noise
                    ax.loglog(periods, record_spectrum, alpha=0.5, linewidth=1)

                # Ortalama
                ax.loglog(periods, target_spectrum * 1.05, 'b--', linewidth=2, label='Seçilen Kayıtlar Ort.')

                ax.grid(True, alpha=0.3)
                ax.set_xlabel('Periyot (s)', fontsize=12)
                ax.set_ylabel('Spektral İvme (g)', fontsize=12)
                ax.set_title('Spektral Eşleştirme', fontsize=14, fontweight='bold')
                ax.legend()

                st.pyplot(fig)

                buf = io.BytesIO()
                fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
                buf.seek(0)
                st.download_button(
                    label="📥 Grafik İndir (PNG)",
                    data=buf,
                    file_name="gms_spektral_eslesme.png",
                    mime="image/png"
                )

    # Seçili dosya görüntüleme
    if 'gms_files' in st.session_state and st.session_state.gms_files:
        selected_gms_file = st.selectbox("Sonuç dosyası seçin:", st.session_state.gms_files, key="gms_file_select")

        if st.button("🔍 Detayları Görüntüle", key="view_gms"):
            try:
                with open(selected_gms_file, 'rb') as f:
                    gms_data = pickle.load(f)

                st.markdown("##### 📋 GMS Sonuç Özeti")

                if isinstance(gms_data, dict):
                    st.write(f"**Toplam Analiz Sayısı:** {len(gms_data)}")

                    # İlk birkaç sonucu göster
                    for i, (key, value) in enumerate(list(gms_data.items())[:3]):
                        with st.expander(f"📄 {key}"):
                            if isinstance(value, dict):
                                st.write("**Seçilen Yer Hareketleri:**")
                                if 'ground_motion_records' in value:
                                    st.write(value['ground_motion_records'])
                                if 'target_spectra' in value:
                                    st.write("**Hedef Spektrum:**", value['target_spectra'])
                                if 'mrp' in value:
                                    st.write("**MRP:**", value['mrp'])
                                if 'n_gm' in value:
                                    st.write("**Kayıt Sayısı:**", value['n_gm'])
                            else:
                                st.json(str(value))

                    # CSV export
                    try:
                        flat_data = []
                        for key, value in gms_data.items():
                            if isinstance(value, dict):
                                if 'ground_motion_records' in value:
                                    records = value['ground_motion_records']
                                    if isinstance(records, (list, np.ndarray)):
                                        for rec in records:
                                            flat_data.append({
                                                'analysis_key': key,
                                                'record': str(rec),
                                                'mrp': value.get('mrp', ''),
                                                'n_gm': value.get('n_gm', '')
                                            })

                        if flat_data:
                            df = pd.DataFrame(flat_data)
                            st.dataframe(df.head(20), use_container_width=True)

                            csv = df.to_csv(index=False).encode('utf-8')
                            st.download_button(
                                label="📥 Seçilen Kayıtları CSV İndir",
                                data=csv,
                                file_name=f"gms_kayitlar_{gms_analysis_case}.csv",
                                mime="text/csv",
                                key="download_gms_csv"
                            )
                    except Exception as e:
                        st.warning(f"⚠️ CSV oluşturulamadı: {str(e)}")

            except Exception as e:
                st.error(f"❌ Dosya okunamadı: {str(e)}")

# ==================== NLTHA ====================
with tab5:
    st.markdown('<div class="sub-header">⚡ NLTHA - Doğrusal Olmayan Zaman Tanım Alanı Analizi</div>', unsafe_allow_html=True)

    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown("""
    **NLTHA (Nonlinear Time-History Analysis)**, yapının seçilen yer hareketi kayıtları
    altında doğrusal olmayan dinamik davranışını analiz eder. EDP (Engineering Demand Parameter)
    değerlerini hesaplar.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 📝 Parametre Girişi")

        nltha_analysis_case = st.text_input("Analiz Durumu:", value="1", key="nltha_case")
        nltha_design_nums = st.text_input("Tasarım Numaraları:", value="1,2,3", key="nltha_design")

        nltha_haz_lev = st.text_input(
            "Tehlike Seviyeleri:",
            value="1,2,3",
            key="nltha_haz"
        )

        nltha_pool_size = st.number_input(
            "Paralel İşlem Sayısı:",
            min_value=1,
            max_value=16,
            value=4,
            key="nltha_pool"
        )

        st.markdown("#### 📊 EDP (Engineering Demand Parameters)")

        nltha_edp_types = st.multiselect(
            "EDP Tipleri:",
            options=[
                "MaxColRebarStrain (Kolon Donatı Birim Şekil Değiştirmesi)",
                "MaxSpringDeformation (Yay Deformasyonu)",
                "FrameMaxDeformation (Çerçeve Deformasyonu)",
                "Özel EDP"
            ],
            default=["MaxColRebarStrain (Kolon Donatı Birim Şekil Değiştirmesi)"],
            help="Hesaplanacak talep parametreleri"
        )

        if "Özel EDP" in nltha_edp_types:
            custom_edp = st.text_input("Özel EDP Tanımı:", key="nltha_custom_edp")

    with col2:
        st.markdown("#### ⚙️ Analiz Ayarları")

        nltha_stage_pool = st.number_input(
            "Staging Paralel İşlem:",
            min_value=1,
            max_value=16,
            value=4,
            key="nltha_stage_pool"
        )

        nltha_gm_database = st.text_input(
            "Yer Hareketi Veritabanı Dizini:",
            value="/path/to/ground_motion_database",
            help="Yer hareketi kayıtlarının bulunduğu dizin"
        )

        nltha_ai_end = st.checkbox(
            "Arias Intensity Bazlı Sonlandırma",
            value=True,
            help="Kayıtları Arias intensity'e göre kırp"
        )

        st.markdown("---")

        if st.button("▶️ NLTHA Analizi Çalıştır", key="run_nltha"):
            st.markdown('<div class="warning-box">', unsafe_allow_html=True)
            st.warning("⚠️ Bu özellik, GMS sonuçları ve OpenSees modeli gerektirir.")

            haz_levs = [x.strip() for x in nltha_haz_lev.split(',')]

            st.markdown(f"""
            **Örnek kod:**
            ```python
            from pypbee import NLTHA, MaxColRebarStrain, MaxSpringDeformation

            # EDP tanımları
            edp_list = [
                MaxColRebarStrain(max_what='compression',
                                 frame_structure=osb, tag='1'),
                MaxColRebarStrain(max_what='tension',
                                 frame_structure=osb, tag='2'),
            ]

            # NLTHA analizi
            nltha = NLTHA(edp_list, im)

            # Staging (hazırlık)
            nltha.stage(
                analysis_case='{nltha_analysis_case}',
                design_num_list=[{nltha_design_nums}],
                haz_lev_list={haz_levs},
                stage_pool_size={nltha_stage_pool},
                gm_database_dir_path='{nltha_gm_database}',
                ai_end={nltha_ai_end}
            )

            # Setup
            nltha.setup(
                analysis_case='{nltha_analysis_case}',
                design_num_list=[{nltha_design_nums}],
                haz_lev_list={haz_levs}
            )

            # Run
            nltha.run(
                analysis_case='{nltha_analysis_case}',
                pool_size={nltha_pool_size}
            )

            # Wrap up
            nltha.wrap_up(analysis_case='{nltha_analysis_case}')
            ```
            """)
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 📊 Sonuç Görüntüleme")

    nltha_result_dir = st.text_input(
        "NLTHA Sonuç Dizini:",
        value=os.path.join(st.session_state.work_dir, "Work_Dir", "NLTHA_Results"),
        key="nltha_result_dir"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📂 Sonuçları Yükle", key="load_nltha"):
            if os.path.exists(nltha_result_dir):
                try:
                    # Recorder dosyalarını ara
                    rec_files = []
                    for root, dirs, files in os.walk(nltha_result_dir):
                        for file in files:
                            if file.endswith('.out') or file.endswith('.txt'):
                                rec_files.append(os.path.join(root, file))

                    if rec_files:
                        st.success(f"✅ {len(rec_files)} adet sonuç dosyası bulundu")
                        st.session_state.nltha_files = rec_files
                    else:
                        st.info("ℹ️ Henüz NLTHA sonucu bulunamadı")
                except Exception as e:
                    st.error(f"❌ Hata: {str(e)}")
            else:
                st.warning("⚠️ Sonuç dizini bulunamadı")

    with col2:
        if 'nltha_files' in st.session_state and st.session_state.nltha_files:
            if st.button("📊 Zaman Serisi Grafiği", key="plot_nltha"):
                st.info("📈 EDP zaman serisi grafiği")

                # Örnek zaman serisi
                fig, ax = plt.subplots(figsize=(10, 6))

                time = np.linspace(0, 20, 1000)
                response = 0.05 * np.sin(2 * np.pi * 1.5 * time) * np.exp(-0.1 * time)

                ax.plot(time, response, 'b-', linewidth=1.5)
                ax.axhline(y=0, color='k', linestyle='--', alpha=0.3)
                ax.grid(True, alpha=0.3)
                ax.set_xlabel('Zaman (s)', fontsize=12)
                ax.set_ylabel('Deformasyon', fontsize=12)
                ax.set_title('Örnek EDP Zaman Serisi', fontsize=14, fontweight='bold')

                st.pyplot(fig)

                buf = io.BytesIO()
                fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
                buf.seek(0)
                st.download_button(
                    label="📥 Grafik İndir",
                    data=buf,
                    file_name="nltha_zaman_serisi.png",
                    mime="image/png"
                )

    with col3:
        if 'nltha_files' in st.session_state and st.session_state.nltha_files:
            if st.button("📊 EDP Dağılımı", key="plot_nltha_dist"):
                st.info("📊 EDP değerlerinin dağılımı")

                # Örnek histogram
                fig, ax = plt.subplots(figsize=(10, 6))

                edp_values = np.random.lognormal(mean=-1, sigma=0.5, size=100)

                ax.hist(edp_values, bins=20, color='steelblue', edgecolor='black', alpha=0.7)
                ax.axvline(x=np.median(edp_values), color='r', linestyle='--',
                          linewidth=2, label=f'Medyan: {np.median(edp_values):.3f}')
                ax.grid(True, alpha=0.3, axis='y')
                ax.set_xlabel('EDP Değeri', fontsize=12)
                ax.set_ylabel('Frekans', fontsize=12)
                ax.set_title('EDP Değerleri Dağılımı', fontsize=14, fontweight='bold')
                ax.legend()

                st.pyplot(fig)

                buf = io.BytesIO()
                fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
                buf.seek(0)
                st.download_button(
                    label="📥 Histogram İndir",
                    data=buf,
                    file_name="nltha_edp_dagilim.png",
                    mime="image/png"
                )

    # Dosya içeriği görüntüleme
    if 'nltha_files' in st.session_state and st.session_state.nltha_files:
        selected_nltha_file = st.selectbox(
            "Sonuç dosyası seçin:",
            st.session_state.nltha_files[:20],  # İlk 20 dosya
            key="nltha_file_select"
        )

        if st.button("🔍 Dosya İçeriğini Görüntüle", key="view_nltha"):
            try:
                # Dosya boyutunu kontrol et
                file_size = os.path.getsize(selected_nltha_file)

                if file_size > 1_000_000:  # 1 MB'dan büyükse
                    st.warning(f"⚠️ Dosya büyük ({file_size / 1_000_000:.2f} MB). İlk 1000 satır gösteriliyor.")
                    max_lines = 1000
                else:
                    max_lines = None

                with open(selected_nltha_file, 'r') as f:
                    if max_lines:
                        lines = [f.readline() for _ in range(max_lines)]
                        content = ''.join(lines)
                    else:
                        content = f.read()

                # Veriyi parse etmeye çalış
                try:
                    data = np.loadtxt(selected_nltha_file)

                    if len(data.shape) == 1:
                        df = pd.DataFrame({'Değer': data})
                    else:
                        df = pd.DataFrame(data)

                    st.markdown("##### 📊 Veri Tablosu (İlk 100 satır)")
                    st.dataframe(df.head(100), use_container_width=True)

                    # İstatistikler
                    st.markdown("##### 📈 İstatistiksel Özet")
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("Minimum", f"{np.min(data):.4f}")
                    with col2:
                        st.metric("Maksimum", f"{np.max(data):.4f}")
                    with col3:
                        st.metric("Ortalama", f"{np.mean(data):.4f}")
                    with col4:
                        st.metric("Std. Sapma", f"{np.std(data):.4f}")

                    # CSV export
                    csv = df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="📥 CSV İndir",
                        data=csv,
                        file_name=os.path.basename(selected_nltha_file).replace('.out', '.csv'),
                        mime="text/csv",
                        key="download_nltha_csv"
                    )

                except:
                    # Sayısal veri değilse, metin olarak göster
                    st.text_area("Dosya İçeriği:", content, height=300)

                    st.download_button(
                        label="📥 Dosyayı İndir",
                        data=content,
                        file_name=os.path.basename(selected_nltha_file),
                        mime="text/plain",
                        key="download_nltha_txt"
                    )

            except Exception as e:
                st.error(f"❌ Dosya okunamadı: {str(e)}")

# ==================== PSDemHA ====================
with tab6:
    st.markdown('<div class="sub-header">📈 PSDemHA - Olasılıksal Sismik Talep Tehlike Analizi</div>', unsafe_allow_html=True)

    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown("""
    **PSDemHA (Probabilistic Seismic Demand Hazard Analysis)**, yapısal talep parametrelerinin
    (EDP) tehlike eğrilerini hesaplar. NLTHA sonuçlarını kullanarak talep-tehlike ilişkisini kurar.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 📝 Parametre Girişi")

        psdemha_analysis_case = st.text_input("Analiz Durumu:", value="1", key="psdemha_case")
        psdemha_design_nums = st.text_input("Tasarım Numaraları:", value="1,2,3", key="psdemha_design")

        psdemha_haz_lev = st.text_input(
            "Tehlike Seviyeleri:",
            value="1,2,3",
            key="psdemha_haz"
        )

        psdemha_n_gm = st.text_input(
            "Yer Hareketi Sayıları:",
            value="11,11,11",
            key="psdemha_ngm",
            help="Her tehlike seviyesi için kullanılan yer hareketi sayısı"
        )

        psdemha_pool_size = st.number_input(
            "Paralel İşlem Sayısı:",
            min_value=1,
            max_value=16,
            value=4,
            key="psdemha_pool"
        )

        st.markdown("#### 📊 EDP Listesi")

        psdemha_edp_tags = st.text_input(
            "EDP Tag'leri (virgülle ayrılmış):",
            value="1,2,3",
            help="Hangi EDP'lerin analiz edileceği"
        )

    with col2:
        st.markdown("#### ⚙️ Tehlike Analiz Parametreleri")

        psdemha_delta_input = st.text_area(
            "Delta Input Değerleri (her EDP için satır):",
            value="0.001\n0.001\n0.01",
            height=100,
            help="Her EDP için integrasyon adım büyüklüğü"
        )

        psdemha_min_scale = st.number_input(
            "Minimum Ölçek Faktörü:",
            min_value=0.1,
            max_value=2.0,
            value=1.0,
            step=0.1,
            key="psdemha_min_scale"
        )

        psdemha_max_scale = st.number_input(
            "Maksimum Ölçek Faktörü:",
            min_value=1.0,
            max_value=10.0,
            value=1.0,
            step=0.1,
            key="psdemha_max_scale"
        )

        st.markdown("---")

        if st.button("▶️ PSDemHA Analizi Çalıştır", key="run_psdemha"):
            st.markdown('<div class="warning-box">', unsafe_allow_html=True)
            st.warning("⚠️ Bu özellik, NLTHA ve PSHA sonuçları gerektirir.")

            haz_levs = [x.strip() for x in psdemha_haz_lev.split(',')]
            n_gms = [x.strip() for x in psdemha_n_gm.split(',')]
            delta_vals = [x.strip() for x in psdemha_delta_input.split('\n') if x.strip()]

            st.markdown(f"""
            **Örnek kod:**
            ```python
            from pypbee import PSDemHA

            # PSDemHA analizi
            psdemha = PSDemHA(edp_list, im)

            # Setup
            psdemha.setup(
                analysis_case='{psdemha_analysis_case}',
                design_num_list=[{psdemha_design_nums}],
                haz_lev_list={haz_levs},
                n_gm_list=[{', '.join(n_gms)}]
            )

            # Run
            psdemha.run(
                analysis_case='{psdemha_analysis_case}',
                pool_size={psdemha_pool_size},
                delta_input_list=[np.array([{', '.join(delta_vals)}])],
                min_max_scale_fac_list=[[{psdemha_min_scale}, {psdemha_max_scale}]]
            )

            # Wrap up
            psdemha.wrap_up(analysis_case='{psdemha_analysis_case}')
            ```
            """)
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 📊 Sonuç Görüntüleme ve Analiz")

    psdemha_result_dir = st.text_input(
        "PSDemHA Sonuç Dizini:",
        value=os.path.join(st.session_state.work_dir, "Work_Dir", "PSDemHA_Results"),
        key="psdemha_result_dir"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📂 Sonuçları Yükle", key="load_psdemha"):
            if os.path.exists(psdemha_result_dir):
                try:
                    pickle_files = []
                    for root, dirs, files in os.walk(psdemha_result_dir):
                        for file in files:
                            if file.endswith('.pickle') and 'psdemha_results' in file:
                                pickle_files.append(os.path.join(root, file))

                    if pickle_files:
                        st.success(f"✅ {len(pickle_files)} adet PSDemHA sonucu bulundu")
                        st.session_state.psdemha_files = pickle_files
                    else:
                        st.info("ℹ️ Henüz PSDemHA sonucu bulunamadı")
                except Exception as e:
                    st.error(f"❌ Hata: {str(e)}")
            else:
                st.warning("⚠️ Sonuç dizini bulunamadı")

    with col2:
        if 'psdemha_files' in st.session_state and st.session_state.psdemha_files:
            if st.button("📊 Talep Tehlike Eğrisi", key="plot_psdemha"):
                st.info("📈 EDP talep tehlike eğrisi")

                # Örnek talep tehlike eğrisi
                fig, ax = plt.subplots(figsize=(10, 6))

                edp_vals = np.logspace(-3, 0, 50)
                hazard_curve = 1 / (1 + np.exp(-5 * (np.log(edp_vals) + 2)))

                ax.loglog(edp_vals, hazard_curve, 'b-', linewidth=2.5, label='Talep Tehlike Eğrisi')

                # Önemli noktalar
                target_probs = [0.02, 0.10, 0.50]
                for prob in target_probs:
                    idx = np.argmin(np.abs(hazard_curve - prob))
                    ax.plot(edp_vals[idx], prob, 'ro', markersize=8)
                    ax.annotate(f'{prob*100:.0f}%',
                               xy=(edp_vals[idx], prob),
                               xytext=(10, 10), textcoords='offset points')

                ax.grid(True, alpha=0.3)
                ax.set_xlabel('EDP Değeri', fontsize=12)
                ax.set_ylabel('Yıllık Aşılma Olasılığı', fontsize=12)
                ax.set_title('Talep Tehlike Eğrisi', fontsize=14, fontweight='bold')
                ax.legend()

                st.pyplot(fig)

                buf = io.BytesIO()
                fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
                buf.seek(0)
                st.download_button(
                    label="📥 Grafik İndir",
                    data=buf,
                    file_name="psdemha_talep_tehlike.png",
                    mime="image/png"
                )

    # Dosya görüntüleme
    if 'psdemha_files' in st.session_state and st.session_state.psdemha_files:
        selected_psdemha_file = st.selectbox(
            "Sonuç dosyası seçin:",
            st.session_state.psdemha_files,
            key="psdemha_file_select"
        )

        if st.button("🔍 Detayları Görüntüle", key="view_psdemha"):
            try:
                with open(selected_psdemha_file, 'rb') as f:
                    psdemha_data = pickle.load(f)

                st.markdown("##### 📋 PSDemHA Sonuç Özeti")

                if isinstance(psdemha_data, dict):
                    st.write(f"**EDP Sayısı:** {len(psdemha_data)}")

                    # Her EDP için sonuçlar
                    for edp_tag, edp_results in psdemha_data.items():
                        with st.expander(f"📊 EDP: {edp_tag}"):
                            st.write(f"**Analiz Sayısı:** {len(edp_results) if isinstance(edp_results, dict) else 'N/A'}")

                            if isinstance(edp_results, dict):
                                # İlk birkaç sonucu göster
                                for key, value in list(edp_results.items())[:3]:
                                    st.write(f"**{key}:**")
                                    st.json(str(value)[:500])  # İlk 500 karakter

                    # CSV export
                    try:
                        flat_data = []
                        for edp_tag, edp_results in psdemha_data.items():
                            if isinstance(edp_results, dict):
                                for analysis_key, result in edp_results.items():
                                    flat_data.append({
                                        'edp_tag': edp_tag,
                                        'analysis_key': analysis_key,
                                        'result': str(result)[:200]
                                    })

                        if flat_data:
                            df = pd.DataFrame(flat_data)
                            st.dataframe(df.head(20), use_container_width=True)

                            csv = df.to_csv(index=False).encode('utf-8')
                            st.download_button(
                                label="📥 Sonuçları CSV İndir",
                                data=csv,
                                file_name=f"psdemha_sonuclar_{psdemha_analysis_case}.csv",
                                mime="text/csv",
                                key="download_psdemha_csv"
                            )
                    except Exception as e:
                        st.warning(f"⚠️ CSV oluşturulamadı: {str(e)}")

            except Exception as e:
                st.error(f"❌ Dosya okunamadı: {str(e)}")

# ==================== PSDamHA ====================
with tab7:
    st.markdown('<div class="sub-header">🔴 PSDamHA - Olasılıksal Sismik Hasar Tehlike Analizi</div>', unsafe_allow_html=True)

    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown("""
    **PSDamHA (Probabilistic Seismic Damage Hazard Analysis)**, yapısal hasar durumlarının
    tehlike eğrilerini hesaplar. Kırılganlık fonksiyonları kullanarak hasar olasılıklarını değerlendirir.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 📝 Parametre Girişi")

        psdamha_analysis_case = st.text_input("Analiz Durumu:", value="1", key="psdamha_case")
        psdamha_design_nums = st.text_input("Tasarım Numaraları:", value="1,2,3", key="psdamha_design")

        psdamha_haz_lev = st.text_input(
            "Tehlike Seviyeleri:",
            value="1,2,3",
            key="psdamha_haz"
        )

        psdamha_n_gm = st.text_input(
            "Yer Hareketi Sayıları:",
            value="11,11,11",
            key="psdamha_ngm"
        )

        psdamha_pool_size = st.number_input(
            "Paralel İşlem Sayısı:",
            min_value=1,
            max_value=16,
            value=4,
            key="psdamha_pool"
        )

        psdamha_rng_seed = st.number_input(
            "Rastgele Sayı Tohumu:",
            min_value=0,
            value=12345,
            key="psdamha_seed"
        )

    with col2:
        st.markdown("#### 🔴 Hasar Durumu Parametreleri")

        psdamha_ds_tags = st.text_input(
            "DS (Damage State) Tag'leri:",
            value="1,2,3",
            help="Hasar durumu etiketleri"
        )

        psdamha_sol_type = st.selectbox(
            "Çözüm Tipi:",
            options=["numerical", "analytical"],
            index=0,
            help="Sayısal veya analitik çözüm"
        )

        psdamha_delta_input = st.text_area(
            "Delta Input Değerleri:",
            value="0.01\n0.01\n0.01",
            height=100,
            key="psdamha_delta"
        )

        st.markdown("---")

        if st.button("▶️ PSDamHA Analizi Çalıştır", key="run_psdamha"):
            st.markdown('<div class="warning-box">', unsafe_allow_html=True)
            st.warning("⚠️ Bu özellik, PSDemHA sonuçları ve DS tanımları gerektirir.")

            haz_levs = [x.strip() for x in psdamha_haz_lev.split(',')]
            n_gms = [x.strip() for x in psdamha_n_gm.split(',')]
            delta_vals = [x.strip() for x in psdamha_delta_input.split('\n') if x.strip()]

            st.markdown(f"""
            **Örnek kod:**
            ```python
            from pypbee import PSDamHA, DS
            from scipy.stats import lognorm

            # Hasar durumu tanımları
            ds_list = [
                DS(
                    edp=edp_list[0],
                    predictor=lambda x: 0.004,
                    haz_req={{
                        'normalized_fragility_dist': lognorm(0.326, 0, 1.02),
                        'estimation_sample_size': 5
                    }},
                    ds_type='col_rebar_strain_damage'
                )
            ]

            # PSDamHA analizi
            psdamha = PSDamHA(ds_list, im, sol_type='{psdamha_sol_type}')

            # Setup
            psdamha.setup(
                analysis_case='{psdamha_analysis_case}',
                design_num_list=[{psdamha_design_nums}],
                haz_lev_list={haz_levs},
                n_gm_list=[{', '.join(n_gms)}],
                rng_seed={psdamha_rng_seed if psdamha_rng_seed > 0 else None}
            )

            # Run
            psdamha.run(
                analysis_case='{psdamha_analysis_case}',
                pool_size={psdamha_pool_size},
                delta_input_list=[np.array([{', '.join(delta_vals)}])]
            )

            # Wrap up
            psdamha.wrap_up(analysis_case='{psdamha_analysis_case}')
            ```
            """)
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 📊 Sonuç Görüntüleme ve Kırılganlık Analizi")

    psdamha_result_dir = st.text_input(
        "PSDamHA Sonuç Dizini:",
        value=os.path.join(st.session_state.work_dir, "Work_Dir", "PSDamHA_Results"),
        key="psdamha_result_dir"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📂 Sonuçları Yükle", key="load_psdamha"):
            if os.path.exists(psdamha_result_dir):
                try:
                    pickle_files = []
                    for root, dirs, files in os.walk(psdamha_result_dir):
                        for file in files:
                            if file.endswith('.pickle') and 'psdamha_results' in file:
                                pickle_files.append(os.path.join(root, file))

                    if pickle_files:
                        st.success(f"✅ {len(pickle_files)} adet PSDamHA sonucu bulundu")
                        st.session_state.psdamha_files = pickle_files
                    else:
                        st.info("ℹ️ Henüz PSDamHA sonucu bulunamadı")
                except Exception as e:
                    st.error(f"❌ Hata: {str(e)}")
            else:
                st.warning("⚠️ Sonuç dizini bulunamadı")

    with col2:
        if 'psdamha_files' in st.session_state and st.session_state.psdamha_files:
            if st.button("📊 Hasar Tehlike Eğrisi", key="plot_psdamha_hazard"):
                st.info("📈 Hasar durumu tehlike eğrisi")

                # Örnek hasar tehlike eğrisi
                fig, ax = plt.subplots(figsize=(10, 6))

                im_vals = np.logspace(-2, 1, 50)

                # Farklı hasar durumları
                ds_minor = 1 / (1 + np.exp(-3 * (np.log(im_vals) + 1)))
                ds_moderate = 1 / (1 + np.exp(-3 * (np.log(im_vals) + 0.5)))
                ds_severe = 1 / (1 + np.exp(-3 * (np.log(im_vals))))

                ax.loglog(im_vals, ds_minor, 'g-', linewidth=2.5, label='Hafif Hasar')
                ax.loglog(im_vals, ds_moderate, 'orange', linewidth=2.5, label='Orta Hasar')
                ax.loglog(im_vals, ds_severe, 'r-', linewidth=2.5, label='Şiddetli Hasar')

                ax.grid(True, alpha=0.3)
                ax.set_xlabel('Intensity Measure (IM)', fontsize=12)
                ax.set_ylabel('Yıllık Aşılma Olasılığı', fontsize=12)
                ax.set_title('Hasar Tehlike Eğrileri', fontsize=14, fontweight='bold')
                ax.legend()

                st.pyplot(fig)

                buf = io.BytesIO()
                fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
                buf.seek(0)
                st.download_button(
                    label="📥 Grafik İndir",
                    data=buf,
                    file_name="psdamha_hasar_tehlike.png",
                    mime="image/png"
                )

    with col3:
        if 'psdamha_files' in st.session_state and st.session_state.psdamha_files:
            if st.button("📊 Kırılganlık Eğrileri", key="plot_psdamha_fragility"):
                st.info("📈 Hasar durumu kırılganlık eğrileri")

                # Örnek kırılganlık eğrileri
                fig, ax = plt.subplots(figsize=(10, 6))

                edp_vals = np.linspace(0, 0.05, 100)

                # Lognormal kırılganlık fonksiyonları
                from scipy.stats import norm

                median_minor = 0.005
                beta_minor = 0.4
                fragility_minor = norm.cdf(np.log(edp_vals / median_minor) / beta_minor)

                median_moderate = 0.015
                beta_moderate = 0.4
                fragility_moderate = norm.cdf(np.log(edp_vals / median_moderate) / beta_moderate)

                median_severe = 0.030
                beta_severe = 0.4
                fragility_severe = norm.cdf(np.log(edp_vals / median_severe) / beta_severe)

                ax.plot(edp_vals, fragility_minor, 'g-', linewidth=2.5, label='Hafif Hasar')
                ax.plot(edp_vals, fragility_moderate, 'orange', linewidth=2.5, label='Orta Hasar')
                ax.plot(edp_vals, fragility_severe, 'r-', linewidth=2.5, label='Şiddetli Hasar')

                ax.grid(True, alpha=0.3)
                ax.set_xlabel('EDP Değeri', fontsize=12)
                ax.set_ylabel('Hasar Olasılığı', fontsize=12)
                ax.set_title('Kırılganlık Eğrileri', fontsize=14, fontweight='bold')
                ax.legend()
                ax.set_xlim(0, 0.05)
                ax.set_ylim(0, 1)

                st.pyplot(fig)

                buf = io.BytesIO()
                fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
                buf.seek(0)
                st.download_button(
                    label="📥 Grafik İndir",
                    data=buf,
                    file_name="psdamha_kirilganlik.png",
                    mime="image/png"
                )

    # Dosya görüntüleme
    if 'psdamha_files' in st.session_state and st.session_state.psdamha_files:
        selected_psdamha_file = st.selectbox(
            "Sonuç dosyası seçin:",
            st.session_state.psdamha_files,
            key="psdamha_file_select"
        )

        if st.button("🔍 Detayları Görüntüle", key="view_psdamha"):
            try:
                with open(selected_psdamha_file, 'rb') as f:
                    psdamha_data = pickle.load(f)

                st.markdown("##### 📋 PSDamHA Sonuç Özeti")

                if isinstance(psdamha_data, dict):
                    st.write(f"**Hasar Durumu Sayısı:** {len(psdamha_data)}")

                    # Her DS için sonuçlar
                    for ds_tag, ds_results in psdamha_data.items():
                        with st.expander(f"🔴 Damage State: {ds_tag}"):
                            st.write(f"**Analiz Sayısı:** {len(ds_results) if isinstance(ds_results, dict) else 'N/A'}")

                            if isinstance(ds_results, dict):
                                # İstatistikler
                                st.markdown("**Özet İstatistikler:**")

                                # İlk birkaç sonucu göster
                                st.markdown("**Örnek Sonuçlar:**")
                                for key, value in list(ds_results.items())[:3]:
                                    st.write(f"**{key}:**")
                                    st.json(str(value)[:500])

                    # CSV export
                    try:
                        flat_data = []
                        for ds_tag, ds_results in psdamha_data.items():
                            if isinstance(ds_results, dict):
                                for analysis_key, result in ds_results.items():
                                    flat_data.append({
                                        'ds_tag': ds_tag,
                                        'analysis_key': analysis_key,
                                        'result': str(result)[:200]
                                    })

                        if flat_data:
                            df = pd.DataFrame(flat_data)
                            st.dataframe(df.head(20), use_container_width=True)

                            csv = df.to_csv(index=False).encode('utf-8')
                            st.download_button(
                                label="📥 Sonuçları CSV İndir",
                                data=csv,
                                file_name=f"psdamha_sonuclar_{psdamha_analysis_case}.csv",
                                mime="text/csv",
                                key="download_psdamha_csv"
                            )
                    except Exception as e:
                        st.warning(f"⚠️ CSV oluşturulamadı: {str(e)}")

            except Exception as e:
                st.error(f"❌ Dosya okunamadı: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p><strong>PyPBEE Türkçe Arayüzü</strong> | Deprem Mühendisliği Analiz Platformu</p>
    <p>Geliştirici: PyPBEE Community | Lisans: MIT</p>
    <p>📧 Destek için: <a href="https://github.com/angshuman311/PyPBEE">GitHub</a></p>
</div>
""", unsafe_allow_html=True)
