# 🎓 TUM Graduation Ceremony: A Curious Student's Event Analysis

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](#)
[![Dataset](https://img.shields.io/badge/Transcript-1%2C641_Lines-blueviolet.svg)](#)
[![Duration](https://img.shields.io/badge/Stream_Duration-03%3A45%3A28-orange.svg)](#)
[![Total Seconds](https://img.shields.io/badge/Total_Seconds-13%2C528s-green.svg)](#)
[![Graduates](https://img.shields.io/badge/Exact_Graduates-3%2C281_Total-red.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](#)

<p align="center">
  <img src="graduation_workspace.jpg" alt="TUM Graduation Analysis Workspace" width="750" />
</p>

> *"My mum kept asking me how the graduation ceremony order would be. I honestly didn't know—I've never attended one before. I figured I could just watch the recording of last year's proceedings, but when I opened it: damn, nearly 4 hours long (13,528 seconds)? But then I realized: there's a transcript. I bet I can pull that transcript from YouTube.*  
> *I didn't think I'd have to download the whole page; I just wanted to make a clean API call. But the endpoint wouldn't give me the subtitles due to rate limits (HTTP 429). So I dispatched an AI agent inside a browser sandbox to extract the raw transcript, and used agentic coding tools to parse and map the timeline.*  
> *I inspected the code functions myself to verify the extraction logic and make sure I wasn't getting hallucinated transcripts. Then came the human observation: I cross-referenced the video against every single timestamp, confirmed the deans' calls, verified the spoken cues, and checked the exact second of the tassel flip so the numbers are accurate to the teeth."*  
> — **P.S. Built with agentic coding tools & verified by human eyes and code review.**

---

## 📊 Core Empirical Dataset Statistics (Accurate to the Teeth)

* **Video Runtime:** **03:45:28** (`13,528 seconds`)
* **Transcript Total Lines:** **1,641 lines** (122,185 characters)
* **First Utterance:** [`00:01`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=1s) *(Cadets entrance)*
* **Last Utterance:** [`03:44:13`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=3h44m13s) *(Recession music)*
* **Official Total Graduates:** **3,281 candidates** (Confirmed at Line 518 [`01:16:03`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=1h16m03s), Line 627 [`01:30:26`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=1h30m26s), and Line 1635 [`03:42:56`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=3h42m56s))
* **Statutory Ceremonial Phases:** **18 distinct epochs**

---

## ⏱️ Calibrated Chronological Event Timeline

Every timestamp below corresponds to the exact line in [12th_graduation_ceremony_transcript.txt](12th_graduation_ceremony_transcript.txt):

| Phase | Start Time | Line # | Duration | Ceremonial Milestone | Key Spoken Cues & Direct Transcript Evidence |
| :-: | :---: | :-: | :-: | :--- | :--- |
| **01** | [`00:01`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=1s) | Line 1 | 4m 16s | **Academic Procession** | [`00:01`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=1s) *"Those are our cadets marching in."* • Deans, Council & VC enter. |
| **02** | [`04:17`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=4m17s) | Line 35 | 10m 51s | **Parade Review & Anthems** | [`04:17`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=4m17s) *"Captain Talib to lead us in the national anthem..."* • Kenya, EAC, and TUM Anthems. |
| **03** | [`15:08`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=15m08s) | Line 112 | 9m 10s | **Interfaith Opening Prayers** | [`15:08`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=15m08s) Sheikh Abdurrahman Said (Du'a) • [`19:25`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=19m25s) Rev. Julius Nudi (Christian prayer). |
| **04** | [`24:18`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=24m18s) | Line 175 | 2m 47s | **Constitution of Congregation** | [`24:18`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=24m18s) Call to VC • [`25:09`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=25m09s) VC: *"I declare this assembly as the 12th congregation..."* |
| **05** | [`27:05`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=27m05s) | Line 190 | 17m 38s | **Announcements & TUM Choir** | [`27:05`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=27m05s) TUM Choir performs *Mateso* (by Rajab Mzee) and spoken-word poetry. |
| **06** | [`44:43`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=44m43s) | Line 308 | 22m 06s | **Valedictorians & Awards** | [`44:43`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=44m43s) Terry Charity Wangui Mugo & Marera Nelson Mandela • [`59:06`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=59m06s) Agono Boniface. |
| **07** | [`01:06:49`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=1h06m49s) | Line 463 | 21m 35s | **Vice Chancellor Address** | [`01:06:49`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=1h06m49s) VC invited • [`01:15:09`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=1h15m09s) VC address begins: [`01:16:03`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=1h16m03s) *"A total of 3,281 students..."* |
| **08** | [`01:28:24`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=1h28m24s) | Line 615 | 9m 02s | **Council Chairman Address** | [`01:28:24`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=1h28m24s) Council Chairman & Acting Chancellor governance report. |
| **09** | [`01:37:26`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=1h37m26s) | Line 680 | 16m 02s | **Chief Guest Address** | [`01:37:26`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=1h37m26s) Chief Guest invited • [`01:39:00`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=1h39m00s) Greetings from CS Education Hon. Julius Migos Ogamba. |
| **10** | [`01:53:28`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=1h53m28s) | Line 801 | 15m 29s | **PhD Degrees Conferment** | [`01:53:28`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=1h53m28s) PhD presentation & conferment • [`02:06:49`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=2h06m49s) Dais photo session. |
| **11** | [`02:08:57`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=2h08m57s) | Line 939 | 7m 38s | **Master's Degrees Conferment** | [`02:08:57`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=2h08m57s) Humanities ➔ Computing ➔ Business ➔ Engineering ➔ Applied Sciences. |
| **12** | [`02:16:35`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=2h16m35s) | Line 997 | 6m 28s | **Institutional Certificates** | [`02:16:35`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=2h16m35s) Certificates presentation • [`02:17:19`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=2h17m19s) Cert in ICT & Maintenance. |
| **13** | [`02:23:03`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=2h23m03s) | Line 1043 | 29m 54s | **University Diplomas Award** | [`02:23:03`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=2h23m03s) Maritime ➔ Computing ➔ Applied Sciences ➔ Business ➔ Engineering. |
| **14** | [`02:52:57`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=2h52m57s) | Line 1259 | 42m 19s | **Bachelor's Roll Call (6 Schools)** | [`02:53:22`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=2h53m22s) Deans called • **[`02:53:42`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=2h53m42s) Computing (ICI) called 1st!** (Full sequence below). |
| **15** | [`03:35:16`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=3h35m16s) | Line 1570 | 2m 48s | **Medical Ethics Oath** | [`03:35:16`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=3h35m16s) Legal Officer administers code of ethics to Medical Lab Science graduates. |
| **16** | [`03:38:04`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=3h38m04s) | Line 1592 | 3m 03s | **Bachelor's Degree Admission** | [`03:38:04`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=3h38m04s) All rise • **[`03:38:46`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=3h38m46s) Chancellor: "I admit the persons presented to me..."** |
| **17** | [`03:41:07`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=3h41m07s) | Line 1619 | 47s | **Congregation Dissolved** | [`03:41:07`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=3h41m07s) Chancellor: *"I declare the 12th congregation dissolved."* |
| **18** | [`03:41:46`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=3h41m46s) | Line 1624 | 2m 27s | **Tassel Flip & Recession** | **[`03:41:46`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=3h41m46s) MC: "Turn tassel from right to left!"** • [`03:41:54`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=3h41m54s) Closing Anthem • [`03:42:56`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=3h42m56s) 3,281 grads valediction. |

---

## 🎓 Exact Undergraduate Sequence & Timestamps

When undergraduate degrees begin at [`02:52:57`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=2h52m57s), the Deans present their cohorts in this exact order:

1. **Institute of Computing and Informatics (ICI):** [`02:53:42`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=2h53m42s) *(BSIT, BSc Computer Science)* — **Line 1264**
2. **School of Applied and Health Sciences (SAHS):** [`02:57:07`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=2h57m07s) *(Medical Lab Science, Food Science)* — **Line 1294**
3. **School of Business (SOB):** [`03:02:35`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=3h02m35s) *(BCom, BBA, Human Resources, Supply Chain)* — **Line 1344**
4. **School of Engineering and Technology (SET):** [`03:10:55`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=3h10m55s) *(Civil, Electrical, Mechanical, Building)* — **Line 1403**
5. **School of Humanities and Social Sciences (SHSS):** [`03:23:33`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=3h23m33s) *(Mass Communication, Development Studies)* — **Line 1493**
6. **Institute of Maritime and Seafaring Studies (IMSS):** [`03:33:04`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=3h33m04s) *(BSc Nautical Science, Maritime Management)* — **Line 1551**

---

## 🎯 The Two Tassel Moments (Distinguished to the Second)

1. **[`03:38:46`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=3h38m46s) (Line 1597) — The Legal Conferment:**  
   The Chancellor pronounces: *"Acting on the powers conferred to me by the Universities Act Cap 210 and the Technical University of Mombasa Charter of 2013... I admit the persons presented to me to the respective degrees of Technical University of Mombasa..."*
2. **[`03:41:46`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=3h41m46s) (Line 1624) — The Spoken Tassel Instruction:**  
   Right after the formal dissolution of the congregation at [`03:41:07`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=3h41m07s), the Master of Ceremonies announces:  
   > *"One minute. Please turn your tassel. Tassel from the right to the left to signify you have graduated."* ([`03:41:46`](https://www.youtube.com/watch?v=6bcyX9n-AQ0&t=3h41m46s))

---

## 💻 Running the Script Locally

```bash
# Clone the repository
git clone https://github.com/userken-arch/tum_graduation_useless_analysis.git
cd tum_graduation_useless_analysis

# Print the calibrated chronological event table
python3 analyze_graduation.py

# Or export to structured JSON
python3 analyze_graduation.py --json > ceremony_timeline.json
```

---

## 📄 License
Open source under the [MIT License](LICENSE). Verified against the raw transcript dataset of the 12th Graduation Ceremony (Class of 2025). 🎓🚀
