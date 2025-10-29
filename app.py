import streamlit as st

st.set_page_config(page_title="Sistem Pakar Rekomendasi Karier", layout="centered")

st.markdown("""
<style>
/* Target container untuk setiap checkbox */
[data-testid="stCheckbox"] {
    background-color: #f0f2f6;
    border-radius: 12px;
    padding: 10px 12px 10px 12px;
    margin-bottom: 8px;
    transition: all 0.2s ease-in-out;
}

/* Efek saat mouse hover di atas chip */
[data-testid="stCheckbox"]:hover {
    background-color: #e6e8eb;
    transform: scale(1.02);
}

/* Menargetkan label (teks) di dalam checkbox */
[data-testid="stCheckbox"] label {
    font-weight: 500;
    color: #31333F;
    cursor: pointer;
}

/* --- PERBAIKAN UNTUK PADDING & GAP --- */
[data-testid="stVerticalBlockBorderWrapper"] div[data-testid="stVerticalBlock"] {
    padding: 1.5rem; /* 24px padding di semua sisi */
    gap: 0.75rem;    /* 12px (defaultnya 1rem atau 16px) */
}
</style>
""", unsafe_allow_html=True)

career_profiles = {
    'Pengembang Perangkat Lunak': {
        'interests_req': ['teknologi'],
        'interests_opt': ['sains'],
        'traits_req': ['analitis', 'teliti'],
        'traits_opt': ['introverted'],
        'job_description': "Merancang, membangun, menguji, dan memelihara perangkat lunak atau aplikasi komputer.",
        'required_skills': ["Bahasa Pemrograman (Python/Java/C++)", "Struktur Data & Algoritma", "Problem Solving"]
    },
    'Desain Grafis': {
        'interests_req': ['seni'],
        'interests_opt': ['teknologi'],
        'traits_req': ['kreatif'],
        'traits_opt': ['mandiri', 'teliti'],
        'job_description': "Membuat konsep visual menggunakan komputer atau tangan, untuk mengkomunikasikan ide yang menginspirasi atau memikat konsumen.",
        'required_skills': ["Adobe Creative Suite (Photoshop, Illustrator)", "Tipografi", "Teori Warna", "Kreativitas"]
    },
    'Dokter': {
        'interests_req': ['kesehatan', 'sains'],
        'interests_opt': [],
        'traits_req': ['analitis'],
        'traits_opt': ['extroverted', 'kerja_tim'],
        'job_description': "Mendiagnosis dan mengobati penyakit serta cedera, memberikan perawatan medis, dan memberi saran kesehatan kepada pasien.",
        'required_skills': ["Ilmu Medis", "Empati", "Pengambilan Keputusan Kritis", "Komunikasi Interpersonal"]
    },
    'Guru': {
        'interests_req': ['pendidikan'],
        'interests_opt': ['layanan_sosial'],
        'traits_req': ['kepemimpinan'],
        'traits_opt': ['extroverted', 'mudah_beradaptasi'],
        'job_description': "Mendidik siswa dengan menyusun rencana pelajaran, mengajar, memberi tugas, dan mengevaluasi kemajuan akademik mereka.",
        'required_skills': ["Komunikasi Publik", "Manajemen Kelas", "Kesabaran", "Perencanaan Kurikulum"]
    },
    'Analis Keuangan': {
        'interests_req': ['keuangan', 'bisnis'],
        'interests_opt': [],
        'traits_req': ['analitis', 'teliti'],
        'traits_opt': ['terorganisir'],
        'job_description': "Menganalisis data keuangan dan tren pasar untuk membantu perusahaan atau individu membuat keputusan investasi yang tepat.",
        'required_skills': ["Analisis Kuantitatif", "Microsoft Excel (Advanced)", "Pemodelan Keuangan", "Pasar Modal"]
    },
    'Penjaga Hutan / Polisi Hutan': {
        'interests_req': ['alam'],
        'interests_opt': ['pekerjaan_fisik', 'layanan_sosial'],
        'traits_req': ['mandiri'],
        'traits_opt': ['mudah_beradaptasi', 'teliti'],
        'job_description': "Melindungi dan mengelola kawasan hutan, satwa liar, dan sumber daya alam, serta memberikan edukasi kepada publik.",
        'required_skills': ["Navigasi & Survival", "Biologi Konservasi", "Kebugaran Fisik", "Komunikasi"]
    },
    'Manajer Pemasaran (Marketing Manager)': {
        'interests_req': ['bisnis'],
        'interests_opt': ['seni'],
        'traits_req': ['kepemimpinan', 'analitis'],
        'traits_opt': ['kreatif', 'extroverted'],
        'job_description': "Merencanakan dan melaksanakan strategi pemasaran untuk mempromosikan produk atau layanan perusahaan.",
        'required_skills': ["Strategi Pemasaran", "SEO/SEM", "Analisis Data", "Komunikasi"]
    },
    'Pekerja Sosial': {
        'interests_req': ['layanan_sosial'],
        'interests_opt': ['kesehatan'],
        'traits_req': [],
        'traits_opt': ['extroverted', 'mudah_beradaptasi', 'kerja_tim'],
        'job_description': "Membantu individu, keluarga, dan komunitas untuk mengatasi tantangan dan meningkatkan kesejahteraan mereka.",
        'required_skills': ["Empati", "Konseling", "Manajemen Kasus", "Advokasi"]
    },
    'Arsitek': {
        'interests_req': ['seni', 'teknologi'],
        'interests_opt': ['sains'],
        'traits_req': ['kreatif', 'analitis'],
        'traits_opt': ['teliti', 'terorganisir'],
        'job_description': "Merancang bangunan dan struktur, menggabungkan aspek fungsionalitas, keamanan, dan estetika.",
        'required_skills': ["Software Desain (AutoCAD, Revit)", "Teori Desain", "Matematika", "Manajemen Proyek"]
    },
    'Ilmuwan Data (Data Scientist)': {
        'interests_req': ['sains', 'teknologi'],
        'interests_opt': ['bisnis'],
        'traits_req': ['analitis', 'teliti'],
        'traits_opt': ['introverted', 'mandiri'],
        'job_description': "Menggunakan metode ilmiah, algoritma, dan sistem untuk mengekstrak wawasan dari data terstruktur dan tidak terstruktur.",
        'required_skills': ["Machine Learning", "Python/R", "Statistika", "Visualisasi Data"]
    },
    'Manajer Proyek (Project Manager)': {
        'interests_req': ['bisnis'],
        'interests_opt': ['teknologi'],
        'traits_req': ['terorganisir', 'kepemimpinan'],
        'traits_opt': ['kerja_tim', 'extroverted'],
        'job_description': "Bertanggung jawab atas perencanaan, pelaksanaan, dan penyelesaian proyek tepat waktu dan sesuai anggaran.",
        'required_skills': ["Manajemen Proyek (Agile/Scrum)", "Penjadwalan", "Komunikasi", "Manajemen Risiko"]
    },
    'Atlet Profesional': {
        'interests_req': ['pekerjaan_fisik'],
        'interests_opt': ['kesehatan'],
        'traits_req': [],
        'traits_opt': ['kerja_tim', 'mandiri', 'mudah_beradaptasi'],
        'job_description': "Berlatih secara intensif dan berkompetisi dalam olahraga di tingkat profesional untuk mencapai prestasi tertinggi.",
        'required_skills': ["Disiplin Tinggi", "Kebugaran Fisik Prima", "Strategi Olahraga", "Ketahanan Mental"]
    },
    'Akuntan': {
        'interests_req': ['keuangan'],
        'interests_opt': ['bisnis'],
        'traits_req': ['teliti', 'terorganisir'],
        'traits_opt': ['analitis', 'introverted'],
        'job_description': "Mencatat, menganalisis, dan melaporkan transaksi keuangan perusahaan serta memastikan kepatuhan pajak.",
        'required_skills': ["Akuntansi Dasar", "Perpajakan", "Software Akuntansi (MYOB/Accurate)", "Analisis Laporan Keuangan"]
    },
    'Perencana Acara (Event Organizer)': {
        'interests_req': ['bisnis'],
        'interests_opt': ['seni', 'layanan_sosial'],
        'traits_req': ['terorganisir'],
        'traits_opt': ['kreatif', 'extroverted', 'kerja_tim'],
        'job_description': "Merencanakan, mengkoordinasikan, dan melaksanakan berbagai acara, mulai dari pernikahan hingga konferensi besar.",
        'required_skills': ["Negosiasi Vendor", "Manajemen Anggaran", "Logistik", "Multitasking"]
    },
    'Petani Modern / Ahli Hortikultura': {
        'interests_req': ['alam', 'sains'],
        'interests_opt': ['bisnis', 'pekerjaan_fisik'],
        'traits_req': ['analitis'],
        'traits_opt': ['mandiri', 'mudah_beradaptasi', 'terorganisir'],
        'job_description': "Mengelola pertanian atau kebun dengan teknik modern (hidroponik, pertanian presisi) untuk meningkatkan efisiensi dan hasil panen.",
        'required_skills': ["Agronomi/Ilmu Tanah", "Manajemen Bisnis Pertanian", "Teknologi Pertanian", "Kebugaran Fisik"]
    }
}

interests = [
    'Teknologi', 'Sains', 'Seni', 'Bisnis', 'Kesehatan',
    'Pendidikan', 'Layanan Sosial', 'Pekerjaan Fisik', 'Alam', 'Keuangan'
]

personality_traits = [
    'Introverted', 'Extroverted', 'Analitis', 'Kreatif', 'Terorganisir',
    'Mudah Beradaptasi', 'Teliti', 'Kepemimpinan', 'Kerja Tim', 'Mandiri'
]

if "page" not in st.session_state:
    st.session_state.page = 0
if "selected_interests" not in st.session_state:
    st.session_state.selected_interests = []
if "selected_traits" not in st.session_state:
    st.session_state.selected_traits = []

def next_page():
    st.session_state.page += 1

def prev_page():
    if st.session_state.page > 0:
        st.session_state.page -= 1

def reset_all():
    for i in range(len(interests)):
        st.session_state[f"interest_{i}"] = False
    for i in range(len(personality_traits)):
        st.session_state[f"trait_{i}"] = False
        
    st.session_state.selected_interests = []
    st.session_state.selected_traits = []
    st.session_state.page = 0

st.title("Sistem Pakar Rekomendasi Karier")

if st.session_state.page == 0:
    with st.container(border=True):
        st.subheader("Selamat Datang!")
        st.write("""
        Ini adalah sistem pakar sederhana yang dirancang untuk membantu Anda menemukan karier yang mungkin cocok berdasarkan dua faktor utama: **minat** dan **sifat kepribadian** Anda.
        """)
        
        st.info("""
        **Cara Melakukan Tes:**
        1.  **Langkah 1:** Anda akan diminta memilih bidang-bidang yang Anda minati.
        2.  **Langkah 2:** Anda akan memilih sifat-sifat yang paling menggambarkan diri Anda.
        3.  **Hasil:** Sistem akan menganalisis pilihan Anda dan memberikan rekomendasi karier.
        """)
        st.write("---")
        st.button(
            "Mulai Tes Sekarang", 
            on_click=next_page, 
            use_container_width=True, 
            type="primary"
        )

elif st.session_state.page == 1:
    with st.container(border=True):
        st.subheader("Langkah 1️⃣ dari 2: Pilih Minat Anda")
        st.progress(50, text="Langkah 1 dari 2")
        st.write("Silakan pilih beberapa bidang yang paling menarik bagi Anda:")

        cols = st.columns(4)
        selected = []
        for idx, item in enumerate(interests):
            with cols[idx % 4]:
                checked = st.checkbox(item, key=f"interest_{idx}", value=(item.lower().replace(' ', '_') in st.session_state.selected_interests))
                if checked:
                    selected.append(item.lower().replace(' ', '_'))

        st.session_state.selected_interests = selected

        st.write("---")
        
        if not selected:
            st.warning("Pilih minimal satu minat untuk melanjutkan.")
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.button(
                "Kembali", 
                on_click=prev_page, 
                use_container_width=True
            )
        with col2:
            st.button(
                "Lanjut ke Sifat Kepribadian", 
                on_click=next_page, 
                use_container_width=True, 
                type="primary",
                disabled=not selected
            )

elif st.session_state.page == 2:
    with st.container(border=True):
        st.subheader("Langkah 2️⃣ dari 2: Pilih Karakter Anda")
        st.progress(100, text="Langkah 2 dari 2")
        st.write("Pilih beberapa sifat yang paling menggambarkan diri Anda:")

        cols = st.columns(4)
        selected = []
        for idx, item in enumerate(personality_traits):
            with cols[idx % 4]:
                checked = st.checkbox(item, key=f"trait_{idx}", value=(item.lower().replace(' ', '_') in st.session_state.selected_traits))
                if checked:
                    selected.append(item.lower().replace(' ', '_'))

        st.session_state.selected_traits = selected

        st.write("---")
        
        if not selected:
            st.warning("Pilih minimal satu sifat kepribadian untuk melanjutkan.")

        col1, col2 = st.columns([1, 2])
        with col1:
            st.button(
                "Kembali ke Minat", 
                on_click=prev_page, 
                use_container_width=True
            )
        with col2:
            st.button(
                "Lihat Hasil Rekomendasi 🔍", 
                on_click=next_page, 
                use_container_width=True, 
                type="primary",
                disabled=not selected
            )

elif st.session_state.page == 3:
    with st.container(border=True):
        st.subheader("📊 Hasil Rekomendasi Karier Anda")
        st.progress(100, text="Selesai!")

        selected_i_set = set(st.session_state.selected_interests)
        selected_t_set = set(st.session_state.selected_traits)

        results = {}
        for career, data in career_profiles.items():
            score = 0
            
            db_int_req = set([i.replace(' ', '_') for i in data.get('interests_req', [])])
            db_int_opt = set([i.replace(' ', '_') for i in data.get('interests_opt', [])])
            db_trt_req = set([i.replace(' ', '_') for i in data.get('traits_req', [])])
            db_trt_opt = set([i.replace(' ', '_') for i in data.get('traits_opt', [])])

            score += len(selected_i_set & db_int_req) * 3
            score += len(selected_t_set & db_trt_req) * 2
            score += len(selected_i_set & db_int_opt) * 1
            score += len(selected_t_set & db_trt_opt) * 1
            
            results[career] = score

        sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

        if not sorted_results or sorted_results[0][1] == 0:
            st.error("Maaf, tidak ada kecocokan kuat yang ditemukan. Coba ubah pilihan Anda.")
        else:
            top_job, top_score = sorted_results[0]
            
            if top_score > 0:
                st.success(f"✨ Karier yang paling cocok untuk Anda adalah: **{top_job}** (Skor: {top_score})")
                
                top_profile = career_profiles[top_job]
                st.write(f"**📝 Deskripsi Pekerjaan:** {top_profile['job_description']}")
                st.write(f"**🔧 Skill Utama:** {', '.join(top_profile['required_skills'])}")

                int_req_match = selected_i_set & set([i.replace(' ', '_') for i in top_profile.get('interests_req', [])])
                int_opt_match = selected_i_set & set([i.replace(' ', '_') for i in top_profile.get('interests_opt', [])])
                trt_req_match = selected_t_set & set([i.replace(' ', '_') for i in top_profile.get('traits_req', [])])
                trt_opt_match = selected_t_set & set([i.replace(' ', '_') for i in top_profile.get('traits_opt', [])])

                details = []
                if int_req_match: details.append(f"Minat Wajib ({', '.join(int_req_match)})")
                if trt_req_match: details.append(f"Sifat Wajib ({', '.join(trt_req_match)})")
                if int_opt_match: details.append(f"Minat Pendukung ({', '.join(int_opt_match)})")
                if trt_opt_match: details.append(f"Sifat Pendukung ({', '.join(trt_opt_match)})")

                st.caption(f"**Cocok karena:** {'; '.join(details)}")
            else:
                st.error("Maaf, tidak ada kecocokan kuat yang ditemukan. Coba ubah pilihan Anda.")

            
            if len(sorted_results) > 1:
                st.write("---")
                st.write("### 🔍 Rekomendasi Lainnya:")
                
                found_other = False
                for job, score in sorted_results[1:]:
                    if score > 2: 
                        found_other = True
                        with st.expander(f"**{job}** (Skor Kecocokan: {score})"):
                            profile = career_profiles[job]
                            st.write(f"**📝 Deskripsi Pekerjaan:** {profile['job_description']}")
                            st.write(f"**🔧 Skill Utama:** {', '.join(profile['required_skills'])}")
                            
                            int_req_match = selected_i_set & set([i.replace(' ', '_') for i in profile.get('interests_req', [])])
                            int_opt_match = selected_i_set & set([i.replace(' ', '_') for i in profile.get('interests_opt', [])])
                            trt_req_match = selected_t_set & set([i.replace(' ', '_') for i in profile.get('traits_req', [])])
                            trt_opt_match = selected_t_set & set([i.replace(' ', '_') for i in profile.get('traits_opt', [])])

                            details = []
                            if int_req_match: details.append(f"Minat Wajib ({', '.join(int_req_match)})")
                            if trt_req_match: details.append(f"Sifat Wajib ({', '.join(trt_req_match)})")
                            if int_opt_match: details.append(f"Minat Pendukung ({', '.join(int_opt_match)})")
                            if trt_opt_match: details.append(f"Sifat Pendukung ({', '.join(trt_opt_match)})")
                            
                            st.caption(f"**Cocok karena:** {'; '.join(details)}")
                
                if not found_other and top_score > 0:
                    st.info("Tidak ada rekomendasi lain yang cocok dengan skor di atas 2.")
                elif not found_other and top_score == 0:
                    pass

        st.write("---")
        st.button(
            "🔁 Ulangi Tes", 
            on_click=reset_all, 
            use_container_width=True
        )

