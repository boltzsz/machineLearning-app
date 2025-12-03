
import streamlit as st
import pandas as pd
import numpy as np

st.title("My First Streamlit App")
st.write("Hello, Streamlit!")

import streamlit as st

def create_input_form():
    st.title("Form Input Data Pasien ECG")
    st.subheader("Silakan masukkan data pasien")
    
    # Membagi layout menjadi dua kolom
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Data Demografi")
        
        # Fitur kategorikal - Demografi
        sex = st.selectbox(
            "Jenis Kelamin (Sex)",
            options=["Male", "Female", "Other", "Unknown"],
            help="Pilih jenis kelamin pasien"
        )
        
        location_setting = st.selectbox(
            "Lokasi Pengaturan (Location Setting)",
            options=["Inpatient", "Outpatient", "Emergency", "Unknown"],
            help="Lokasi pemeriksaan dilakukan"
        )
        
        race_ethnicity = st.selectbox(
            "Ras/Etnis (Race/Ethnicity)",
            options=["Asian", "White", "Black", "Hispanic", "Other", "Unknown"],
            help="Pilih ras/etnis pasien"
        )
        
        # Fitur numerik - Umur
        age_at_ecg = st.number_input(
            "Usia saat ECG (Age at ECG)",
            min_value=0,
            max_value=120,
            value=50,
            help="Usia pasien saat pemeriksaan ECG"
        )
        
        # Fitur numerik - Tahun
        acquisition_year = st.number_input(
            "Tahun Pemeriksaan (Acquisition Year)",
            min_value=1900,
            max_value=2100,
            value=2024,
            help="Tahun pemeriksaan ECG dilakukan"
        )
        
        most_recent_ecg = st.number_input(
            "ECG Terbaru (Most Recent ECG)",
            min_value=0,
            max_value=1,
            value=1,
            help="Apakah ini ECG terbaru? (1=Ya, 0=Tidak)"
        )
        
    with col2:
        st.header("Parameter ECG")
        
        # Fitur numerik - Parameter ECG
        ventricular_rate = st.number_input(
            "Laju Ventrikular (Ventricular Rate)",
            min_value=0.0,
            max_value=300.0,
            value=75.0,
            format="%.1f",
            help="Laju ventrikular dalam bpm"
        )
        
        atrial_rate = st.number_input(
            "Laju Atrial (Atrial Rate)",
            min_value=0.0,
            max_value=300.0,
            value=80.0,
            format="%.1f",
            help="Laju atrial dalam bpm"
        )
        
        pr_interval = st.number_input(
            "Interval PR (PR Interval)",
            min_value=0.0,
            max_value=500.0,
            value=160.0,
            format="%.1f",
            help="Interval PR dalam ms"
        )
        
        qrs_duration = st.number_input(
            "Durasi QRS (QRS Duration)",
            min_value=0.0,
            max_value=200.0,
            value=100.0,
            format="%.1f",
            help="Durasi QRS dalam ms"
        )
        
        qt_corrected = st.number_input(
            "QT Corrected",
            min_value=0.0,
            max_value=600.0,
            value=420.0,
            format="%.1f",
            help="QT corrected dalam ms"
        )
        
    # Bagian kedua dari form
    st.header("Pengukuran Ekokardiografi")
    
    # Menggunakan expander untuk mengelompokkan data
    with st.expander("Pengukuran Struktural", expanded=True):
        col3, col4 = st.columns(2)
        
        with col3:
            ivs_measurement = st.number_input(
                "IVS Measurement (mm)",
                min_value=0.0,
                max_value=30.0,
                value=10.0,
                format="%.1f",
                help="Pengukuran interventricular septum"
            )
            
            lvpw_measurement = st.number_input(
                "LVPW Measurement (mm)",
                min_value=0.0,
                max_value=30.0,
                value=10.0,
                format="%.1f",
                help="Pengukuran left ventricular posterior wall"
            )
            
            pasp_value = st.number_input(
                "PASP Value (mmHg)",
                min_value=0.0,
                max_value=100.0,
                value=25.0,
                format="%.1f",
                help="Pulmonary artery systolic pressure"
            )
            
            tr_max_velocity_value = st.number_input(
                "TR Max Velocity Value (m/s)",
                min_value=0.0,
                max_value=5.0,
                value=2.5,
                format="%.1f",
                help="Tricuspid regurgitation max velocity"
            )
        
        with col4:
            # Flag untuk kondisi struktural
            lvwt_gte_13_flag = st.selectbox(
                "LVWT ≥ 13 mm Flag",
                options=[0, 1],
                format_func=lambda x: "Ya" if x == 1 else "Tidak",
                help="Left ventricular wall thickness ≥ 13 mm"
            )
            
            pasp_gte_45_flag = st.selectbox(
                "PASP ≥ 45 mmHg Flag",
                options=[0, 1],
                format_func=lambda x: "Ya" if x == 1 else "Tidak",
                help="Pulmonary artery systolic pressure ≥ 45 mmHg"
            )
            
            tr_max_gte_32_flag = st.selectbox(
                "TR Max ≥ 3.2 m/s Flag",
                options=[0, 1],
                format_func=lambda x: "Ya" if x == 1 else "Tidak",
                help="Tricuspid regurgitation max velocity ≥ 3.2 m/s"
            )
    
    with st.expander("Gangguan Katup Jantung", expanded=False):
        col5, col6 = st.columns(2)
        
        with col5:
            # Fitur kategorikal - Gangguan Katup
            aortic_stenosis_value = st.selectbox(
                "Aortic Stenosis",
                options=["None", "Mild", "Moderate", "Severe", "Unknown"],
                help="Tingkat aortic stenosis"
            )
            
            aortic_regurgitation_value = st.selectbox(
                "Aortic Regurgitation",
                options=["None", "Mild", "Moderate", "Severe", "Unknown"],
                help="Tingkat aortic regurgitation"
            )
            
            mitral_regurgitation_value = st.selectbox(
                "Mitral Regurgitation",
                options=["None", "Mild", "Moderate", "Severe", "Unknown"],
                help="Tingkat mitral regurgitation"
            )
        
        with col6:
            tricuspid_regurgitation_value = st.selectbox(
                "Tricuspid Regurgitation",
                options=["None", "Mild", "Moderate", "Severe", "Unknown"],
                help="Tingkat tricuspid regurgitation"
            )
            
            pulmonary_regurgitation_value = st.selectbox(
                "Pulmonary Regurgitation",
                options=["None", "Mild", "Moderate", "Severe", "Unknown"],
                help="Tingkat pulmonary regurgitation"
            )
    
    with st.expander("Gangguan Lainnya", expanded=False):
        col7, col8 = st.columns(2)
        
        with col7:
            # Fitur kategorikal - Fungsi dan Efusi
            rv_systolic_function_value = st.selectbox(
                "RV Systolic Function",
                options=["Normal", "Mild Dysfunction", "Moderate Dysfunction", "Severe Dysfunction", "Unknown"],
                help="Tingkat fungsi sistolik ventrikel kanan"
            )
            
            pericardial_effusion_value = st.selectbox(
                "Pericardial Effusion",
                options=["None", "Small", "Moderate", "Large", "Unknown"],
                help="Tingkat pericardial effusion"
            )
        
        with col8:
            # Flag untuk kondisi gangguan
            aortic_stenosis_moderate_or_greater_flag = st.selectbox(
                "Aortic Stenosis (Moderate+) Flag",
                options=[0, 1],
                format_func=lambda x: "Ya" if x == 1 else "Tidak",
                help="Aortic stenosis moderate atau lebih berat"
            )
            
            aortic_regurgitation_moderate_or_greater_flag = st.selectbox(
                "Aortic Regurgitation (Moderate+) Flag",
                options=[0, 1],
                format_func=lambda x: "Ya" if x == 1 else "Tidak",
                help="Aortic regurgitation moderate atau lebih berat"
            )
            
            mitral_regurgitation_moderate_or_greater_flag = st.selectbox(
                "Mitral Regurgitation (Moderate+) Flag",
                options=[0, 1],
                format_func=lambda x: "Ya" if x == 1 else "Tidak",
                help="Mitral regurgitation moderate atau lebih berat"
            )
            
            tricuspid_regurgitation_moderate_or_greater_flag = st.selectbox(
                "Tricuspid Regurgitation (Moderate+) Flag",
                options=[0, 1],
                format_func=lambda x: "Ya" if x == 1 else "Tidak",
                help="Tricuspid regurgitation moderate atau lebih berat"
            )
            
            pulmonary_regurgitation_moderate_or_greater_flag = st.selectbox(
                "Pulmonary Regurgitation (Moderate+) Flag",
                options=[0, 1],
                format_func=lambda x: "Ya" if x == 1 else "Tidak",
                help="Pulmonary regurgitation moderate atau lebih berat"
            )
            
            rv_systolic_dysfunction_moderate_or_greater_flag = st.selectbox(
                "RV Dysfunction (Moderate+) Flag",
                options=[0, 1],
                format_func=lambda x: "Ya" if x == 1 else "Tidak",
                help="RV systolic dysfunction moderate atau lebih berat"
            )
            
            pericardial_effusion_moderate_large_flag = st.selectbox(
                "Pericardial Effusion (Moderate/Large) Flag",
                options=[0, 1],
                format_func=lambda x: "Ya" if x == 1 else "Tidak",
                help="Pericardial effusion moderate atau large"
            )
            
            shd_moderate_or_greater_flag = st.selectbox(
                "SHD (Moderate+) Flag",
                options=[0, 1],
                format_func=lambda x: "Ya" if x == 1 else "Tidak",
                help="Structural heart disease moderate atau lebih berat"
            )
    
    # Tombol submit
    if st.button("Submit Data", type="primary"):
        # Mengumpulkan semua data
        data = {
            # Numerik
            'age_at_ecg': age_at_ecg,
            'acquisition_year': acquisition_year,
            'most_recent_ecg': most_recent_ecg,
            'ventricular_rate': ventricular_rate,
            'atrial_rate': atrial_rate,
            'pr_interval': pr_interval,
            'qrs_duration': qrs_duration,
            'qt_corrected': qt_corrected,
            'ivs_measurement': ivs_measurement,
            'lvpw_measurement': lvpw_measurement,
            'pasp_value': pasp_value,
            'tr_max_velocity_value': tr_max_velocity_value,
            
            # Kategorikal
            'sex': sex,
            'location_setting': location_setting,
            'race_ethnicity': race_ethnicity,
            'aortic_stenosis_value': aortic_stenosis_value,
            'aortic_regurgitation_value': aortic_regurgitation_value,
            'mitral_regurgitation_value': mitral_regurgitation_value,
            'tricuspid_regurgitation_value': tricuspid_regurgitation_value,
            'pulmonary_regurgitation_value': pulmonary_regurgitation_value,
            'rv_systolic_function_value': rv_systolic_function_value,
            'pericardial_effusion_value': pericardial_effusion_value,
            
            # Flag
            'lvwt_gte_13_flag': lvwt_gte_13_flag,
            'pasp_gte_45_flag': pasp_gte_45_flag,
            'tr_max_gte_32_flag': tr_max_gte_32_flag,
            'aortic_stenosis_moderate_or_greater_flag': aortic_stenosis_moderate_or_greater_flag,
            'aortic_regurgitation_moderate_or_greater_flag': aortic_regurgitation_moderate_or_greater_flag,
            'mitral_regurgitation_moderate_or_greater_flag': mitral_regurgitation_moderate_or_greater_flag,
            'tricuspid_regurgitation_moderate_or_greater_flag': tricuspid_regurgitation_moderate_or_greater_flag,
            'pulmonary_regurgitation_moderate_or_greater_flag': pulmonary_regurgitation_moderate_or_greater_flag,
            'rv_systolic_dysfunction_moderate_or_greater_flag': rv_systolic_dysfunction_moderate_or_greater_flag,
            'pericardial_effusion_moderate_large_flag': pericardial_effusion_moderate_large_flag,
            'shd_moderate_or_greater_flag': shd_moderate_or_greater_flag
        }
        
        # Menampilkan data yang telah dikumpulkan
        st.success("Data berhasil dikumpulkan!")
        st.json(data)
        
        # Di sini Anda dapat menambahkan logika untuk memproses data lebih lanjut
        # seperti menyimpan ke database atau melakukan prediksi
        
        return data
    
    return None

if __name__ == "__main__":
    create_input_form()



