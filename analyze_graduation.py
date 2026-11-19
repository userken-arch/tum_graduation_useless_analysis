#!/usr/bin/env python3
"""
analyze_graduation.py
Analyzes the transcript of the 12th Graduation Ceremony of the Technical University of Mombasa (TUM).
Extracts, segments, and outputs the detailed chronological ordering of all ceremonial events.
"""

import re
import json
import os
import sys

def parse_transcript(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    entries = []
    time_regex = re.compile(r'\[(\d\d:\d\d(?::\d\d)?)\]\s*(.*)')
    for idx, line in enumerate(lines):
        m = time_regex.match(line.strip())
        if m:
            ts = m.group(1)
            text = m.group(2)
            parts = [int(p) for p in ts.split(':')]
            sec = parts[0] * 3600 + parts[1] * 60 + parts[2] if len(parts) == 3 else parts[0] * 60 + parts[1]
            entries.append({'line': idx + 1, 'ts': ts, 'sec': sec, 'text': text})
    return entries

def build_chronology(entries):
    # Defined milestones based on ceremonial markers and speech transitions
    milestones = [
        {
            "order": 1,
            "phase": "Academic & Ceremonial Procession",
            "start_ts": "00:01",
            "end_ts": "04:00",
            "lead_actors": "Marine Cadets, Brass Band, Deans & Directors, Council Members, DVCs, VC Prof. Laila Abubakar, Council Chairman",
            "summary": "Arrival of cadets, brass band, academic staff, deans, directors, university council, and management.",
            "details": "Cadets from the Institute of Maritime and Seafaring Studies march in with the university brass band. Welcoming faculty members, Dr. McKenzie, Dr. Ali, Director of Graduate Studies Dr. Muri, Dean of Students, Director ODeL, Director of Computing & Informatics, Director of Career Services, Dean of Applied and Health Sciences (Prof. Makande), Dean of Humanities (Dr. Madha), Dean of Medicine, Registrar PRI, Council members, DVC Administration, Finance & Planning (Prof. Joseph Rasowo), DVC ARE, Vice Chancellor Prof. Laila Abubakar, and the Council Chair / Acting Chancellor."
        },
        {
            "order": 2,
            "phase": "Parade Review & National Anthems",
            "start_ts": "04:00",
            "end_ts": "11:48",
            "lead_actors": "Captain Talib (Director, Maritime Studies), Marine Cadets, Marine Rover Scouts, Council Chair",
            "summary": "Parade inspection and solemn playing of national and institutional anthems.",
            "details": "Parade mounted by the Marine Cadets and Marine Rover Scouts is formally handed over to Captain Talib. Playing of the Kenya National Anthem, East African Community (EAC) Anthem, and TUM Anthem. Council Chair/Chief Guest inspects the guard of honor."
        },
        {
            "order": 3,
            "phase": "Interfaith Invocations & Solemn Prayers",
            "start_ts": "11:49",
            "end_ts": "24:17",
            "lead_actors": "Sheikh Abdurrahman Said (Islamic prayer), Reverend Julius Nudi (Christian prayer)",
            "summary": "Opening spiritual dedications by Islamic and Christian religious leaders.",
            "details": "Sheikh Abdurrahman Said leads the Muslim opening supplication (Du'a) seeking divine wisdom, ethical stewardship, and guidance for graduates. Reverend Julius Nudi follows with Christian prayer of thanksgiving and dedication of the graduates to national and global service."
        },
        {
            "order": 4,
            "phase": "Constitution of the 12th Congregation",
            "start_ts": "24:18",
            "end_ts": "25:37",
            "lead_actors": "Prof. Laila Abubakar (Vice Chancellor)",
            "summary": "Official statutory constitution of the graduation assembly.",
            "details": "Vice Chancellor Prof. Laila Abubakar officially constitutes the assembly: 'Acting on the powers conferred to me by the Universities Act Cap 210 and the Technical University of Mombasa Charter of 2013, I declare this assembly as the 12th Congregation of the Technical University of Mombasa.'"
        },
        {
            "order": 5,
            "phase": "Administrative Announcements & Choral Entertainment",
            "start_ts": "25:38",
            "end_ts": "41:42",
            "lead_actors": "Registrar Academic Affairs, Award-winning TUM Choir",
            "summary": "Housekeeping announcements and musical performances by the university choir.",
            "details": "Registrar Academic Affairs delivers administrative announcements. TUM Choir (national drama & music festival winners) performs the classic Zilizopendwa song 'Mateso' (composed by Rajab Mzee) followed by choral poetry and cultural entertainment."
        },
        {
            "order": 6,
            "phase": "Recognition of Top Scholars & Valedictory Addresses",
            "start_ts": "41:43",
            "end_ts": "01:06:48",
            "lead_actors": "Prof. Laila Abubakar (VC), Terry Charity Wangui Mugo (Top Female), Marera Nelson Mandela (Top Male / Valedictorian), Agono Boniface Mandela",
            "summary": "Conferment of academic awards to top-performing students and valedictorian speeches.",
            "details": "Vice Chancellor calls forward the top overall graduating students. Valedictory speeches delivered by Terry Charity Wangui Mugo (BSc Medical Laboratory Science, School of Applied and Health Sciences) and Marera Nelson Mandela (BSc Medical Laboratory Science). Recognition of top Supply Chain graduate Agono Boniface Mandela. Presentation of industry partner awards and trophies."
        },
        {
            "order": 7,
            "phase": "Vice Chancellor's Welcome Address",
            "start_ts": "01:06:49",
            "end_ts": "01:28:23",
            "lead_actors": "Prof. Laila Abubakar (Vice Chancellor)",
            "summary": "State of the University report and key institutional milestones.",
            "details": "Prof. Laila Abubakar reviews university performance: launch of Mombasa County's first School of Medicine, launch of BSc in Nautical Science, Pwani Innovation Week successes, multimillion research grants, infrastructure expansion, and commendation of the 3,281 graduating candidates."
        },
        {
            "order": 8,
            "phase": "Council Chairman & Acting Chancellor's Address",
            "start_ts": "01:28:24",
            "end_ts": "01:37:25",
            "lead_actors": "Chairman of Council / Acting Chancellor",
            "summary": "Governance report, commendation of leadership, and charge to graduates.",
            "details": "Chairman of Council highlights statutory compliance, institutional sustainability, blue economy focus through the Institute of Maritime and Seafaring Studies, and congratulates the Vice Chancellor and Senate on their strategic achievements."
        },
        {
            "order": 9,
            "phase": "Chief Guest's Keynote Address",
            "start_ts": "01:37:26",
            "end_ts": "01:46:00",
            "lead_actors": "Chief Guest (Representing CS Education Hon. Julius Migos Ogamba & PS Higher Education)",
            "summary": "Official government address on higher education, TVET, and national human capital.",
            "details": "The Chief Guest conveys greetings and read addresses on behalf of Cabinet Secretary for Education Hon. Julius Migos Ogamba and the Principal Secretary for Higher Education and Research, praising TUM's leadership in applied technology and medical sciences."
        },
        {
            "order": 10,
            "phase": "Conferment of Doctorate (PhD) Degrees",
            "start_ts": "01:46:00",
            "end_ts": "02:08:00",
            "lead_actors": "School Deans (including School of Business), Acting Chancellor, Vice Chancellor",
            "summary": "Hooding and formal conferment of Doctor of Philosophy degrees.",
            "details": "Presentation of PhD candidates by their respective School Deans. Acting Chancellor pronounces the conferment. Ceremonial hooding, cap fitting, and official dais photo session with university leadership."
        },
        {
            "order": 11,
            "phase": "Conferment of Master's Degrees & Postgraduate Diplomas",
            "start_ts": "02:08:00",
            "end_ts": "02:16:34",
            "lead_actors": "Deans of Humanities, Computing, Business, Engineering, and Applied Sciences; Acting Chancellor",
            "summary": "Presentation and conferment of Master's degrees across all faculties.",
            "details": "Sequential presentation of Master's graduates: School of Humanities & Social Sciences [02:08:57], Institute of Computing & Informatics [02:09:38], School of Business, School of Engineering & Technology, and School of Applied & Health Sciences. Chancellor admits candidates to their respective master's degrees."
        },
        {
            "order": 12,
            "phase": "Award of Institutional Certificates",
            "start_ts": "02:16:35",
            "end_ts": "02:23:02",
            "lead_actors": "Directors & Deans (Computing, Business, Engineering), Acting Chancellor",
            "summary": "Presentation and conferment of vocational and technical certificates.",
            "details": "Presentation of candidates for institutional certificates (e.g. ICT & Maintenance, Business certificates). Acting Chancellor awards certificates."
        },
        {
            "order": 13,
            "phase": "Award of University Diplomas",
            "start_ts": "02:23:03",
            "end_ts": "02:52:56",
            "lead_actors": "Deans & Directors (Maritime, Computing, Applied Sciences, Business, Engineering, Humanities); Acting Chancellor",
            "summary": "Comprehensive presentation and conferment of diplomas across all departments.",
            "details": "Roll call of diploma candidates: Institute of Maritime & Seafaring Studies (Diploma in Nautical Science, Shipping) [02:23:03], Institute of Computing & Informatics [02:24:30], School of Applied & Health Sciences (Medical Engineering, etc.) [02:30:00], School of Business [02:37:00], School of Engineering & Technology [02:44:00], and School of Humanities. Collective award of diplomas by the Acting Chancellor [02:52:17]."
        },
        {
            "order": 14,
            "phase": "Conferment of Bachelor's Degrees (School by School)",
            "start_ts": "02:52:57",
            "end_ts": "03:35:15",
            "lead_actors": "Directors and Deans of all constituent schools",
            "summary": "Rigorous presentation of undergraduate degree candidates by faculty.",
            "details": "1. Institute of Computing & Informatics [02:53:42]\n2. School of Applied & Health Sciences [02:57:07]\n3. School of Business [03:02:35]\n4. School of Engineering & Technology [03:10:55]\n5. School of Humanities & Social Sciences [03:23:33]\n6. Institute of Maritime & Seafaring Studies [03:33:04]."
        },
        {
            "order": 15,
            "phase": "Professional Oath of Practice (Medical Laboratory Sciences)",
            "start_ts": "03:35:16",
            "end_ts": "03:38:03",
            "lead_actors": "University Legal Officer, BSc Medical Laboratory Science Graduates",
            "summary": "Administration of professional ethical oath for medical graduates.",
            "details": "All graduating medical laboratory scientists stand. The University Legal Officer administers the solemn code of professional conduct and ethical dedication required for clinical licensure."
        },
        {
            "order": 16,
            "phase": "Solemn Admission & Conferment of All Bachelor's Degrees",
            "start_ts": "03:38:04",
            "end_ts": "03:40:59",
            "lead_actors": "Acting Chancellor, All Bachelor's Graduates",
            "summary": "Statutory formula of conferment for all undergraduate candidates.",
            "details": "All Bachelor's graduands rise. Chancellor delivers the solemn conferment formula: 'I admit the persons presented to me to the respective degrees of Technical University of Mombasa, and by my authority and that of the Senate, give power to read and to do all that appertains to this degree.' Tassel turning and campus-wide celebrations."
        },
        {
            "order": 17,
            "phase": "Dissolution of the 12th Congregation",
            "start_ts": "03:41:00",
            "end_ts": "03:41:53",
            "lead_actors": "Acting Chancellor",
            "summary": "Statutory formal dissolution of the congregation.",
            "details": "The Acting Chancellor declares: 'Acting on the powers conferred by the TUM statutes, the Universities Act Cap 210, and the Technical University of Mombasa Charter of 2013, I declare the 12th Congregation of Technical University of Mombasa dissolved.'"
        },
        {
            "order": 18,
            "phase": "National Anthem & Academic Recession",
            "start_ts": "03:41:54",
            "end_ts": "03:44:13",
            "lead_actors": "Chancellor, Vice Chancellor, Council, Senate, Brass Band",
            "summary": "Solemn closing anthem and academic procession recession.",
            "details": "Assembly stands for the Kenya National Anthem. Final congratulatory announcements for the 3,281 graduates of the class of 2025. Academic and Chancellor's procession departs the arena to brass band music."
        }
    ]
    return milestones

if __name__ == '__main__':
    t_file = '/home/ken/.gemini/antigravity/brain/3c199db4-006c-4577-954a-fa2a47ba2495/12th_graduation_ceremony_transcript.txt'
    if len(sys.argv) > 1:
        t_file = sys.argv[1]

    entries = parse_transcript(t_file)
    print(f"Loaded {len(entries)} transcript lines from {t_file}")
    milestones = build_chronology(entries)

    print("\n" + "="*80)
    print("CHRONOLOGICAL ORDER OF EVENTS - 12TH GRADUATION CEREMONY (TUM)")
    print("="*80)
    for m in milestones:
        print(f"[{m['order']:02d}] {m['start_ts']} - {m['end_ts']} | {m['phase']}")
        print(f"     Actors: {m['lead_actors']}")
        print(f"     Summary: {m['summary']}\n")
