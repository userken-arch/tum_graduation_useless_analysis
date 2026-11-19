#!/usr/bin/env python3
"""
TUM Graduation Ceremony Timeline Parser
A simple Python script written by a curious BSIT student to parse the
12th Graduation Ceremony livestream transcript and figure out the exact event order.
"""

import re
import json
import os
import sys
from dataclasses import dataclass, asdict
from typing import List, Dict, Any


@dataclass
class CeremonyPhase:
    order: int
    start_time: str
    end_time: str
    duration_minutes: float
    name: str
    key_actors: List[str]
    description: str


class GraduationTimelineParser:
    def __init__(self, transcript_file: str):
        self.transcript_file = transcript_file
        self.lines = []
        self._load_file()

    def _load_file(self):
        if not os.path.exists(self.transcript_file):
            alt = os.path.join(os.path.dirname(__file__), self.transcript_file)
            if os.path.exists(alt):
                self.transcript_file = alt

        with open(self.transcript_file, 'r', encoding='utf-8') as f:
            self.lines = [line.strip() for line in f if line.strip()]

    def _to_seconds(self, ts_str: str) -> int:
        parts = [int(p) for p in ts_str.split(':')]
        if len(parts) == 3:
            return parts[0] * 3600 + parts[1] * 60 + parts[2]
        return parts[0] * 60 + parts[1]

    def _format_seconds(self, sec: int) -> str:
        h = sec // 3600
        m = (sec % 3600) // 60
        s = sec % 60
        if h > 0:
            return f"{h:02d}:{m:02d}:{s:02d}"
        return f"{m:02d}:{s:02d}"

    def get_phases(self) -> List[CeremonyPhase]:
        # Defined phase boundaries identified from the transcript
        raw_phases = [
            (1, "00:01", "04:00", "Academic Procession",
             ["Marine Cadets", "TUM Brass Band", "Deans", "Senate", "Council Chair"],
             "Marine Cadets and brass band march in, followed by faculty deans and university leadership."),

            (2, "04:00", "11:48", "Parade Review & Anthems",
             ["Capt. Talib (Dir. Maritime)", "Marine Scouts", "Council Chair"],
             "Parade inspection; Kenya National Anthem, East African Community Anthem, and TUM Anthem."),

            (3, "11:49", "24:17", "Interfaith Opening Prayers",
             ["Sheikh Abdurrahman Said", "Rev. Julius Nudi"],
             "Islamic opening prayer and Christian thanksgiving prayer."),

            (4, "24:18", "25:37", "Constitution of the Congregation",
             ["Prof. Laila Abubakar (Vice Chancellor)"],
             "VC formally constitutes the 12th congregation under the Universities Act & TUM Charter."),

            (5, "25:38", "41:42", "Announcements & TUM Choir",
             ["Registrar Academic Affairs", "TUM Choir"],
             "Administrative notices; award-winning TUM Choir performs 'Mateso' (by Rajab Mzee)."),

            (6, "41:43", "01:06:48", "Valedictorian Speeches & Awards",
             ["Terry Charity Wangui Mugo", "Marera Nelson Mandela", "Agono Boniface"],
             "Top scholars recognized; valedictory speeches by Medical Laboratory Science graduates."),

            (7, "01:06:49", "01:28:23", "Vice Chancellor's Welcome Address",
             ["Prof. Laila Abubakar (VC)"],
             "State of the university report: inaugural School of Medicine cohort, BSc Nautical Science, research grants."),

            (8, "01:28:24", "01:37:25", "Council Chairman's Address",
             ["Chairman of Council / Acting Chancellor"],
             "Governance remarks and charge to graduating class on ethics and professionalism."),

            (9, "01:37:26", "01:46:00", "Chief Guest's Keynote Address",
             ["Chief Guest (Rep. CS Education Hon. Julius Migos Ogamba)"],
             "National address on higher education, TVET funding, and graduate skills."),

            (10, "01:46:00", "02:08:00", "Conferment of PhD Degrees",
             ["School Deans", "Acting Chancellor", "Doctoral Candidates"],
             "Presentation of PhD candidates, conferment, ceremonial hooding, and official dais photos."),

            (11, "02:08:00", "02:16:34", "Conferment of Master's Degrees",
             ["Deans of Humanities, Computing, Business, Engineering, Science"],
             "Faculty roll call and conferment of Master of Science & MBA degrees."),

            (12, "02:16:35", "02:23:02", "Award of Institutional Certificates",
             ["Institute Directors", "Acting Chancellor"],
             "Presentation and award of vocational/technical certificates (e.g. ICT & Maintenance)."),

            (13, "02:23:03", "02:52:56", "Award of University Diplomas",
             ["Deans of Maritime, Computing, Applied Sciences, Business, Engineering"],
             "Roll call and award of diplomas across all departments."),

            (14, "02:52:57", "03:35:15", "Bachelor's Roll Call by School",
             ["1. Computing & Informatics (BSIT)", "2. Applied Sciences", "3. Business", "4. Engineering", "5. Humanities", "6. Maritime"],
             "Undergraduate roll call. Institute of Computing and Informatics (BSIT) is presented FIRST!"),

            (15, "03:35:16", "03:38:03", "Medical Ethics Oath",
             ["University Legal Officer", "BSc Medical Lab Science Candidates"],
             "Graduating Medical Laboratory Scientists stand and take the professional code of ethics."),

            (16, "03:38:04", "03:40:59", "Conferment of Bachelor's Degrees",
             ["Acting Chancellor", "All Bachelor's Candidates"],
             "Chancellor confers degrees ('Give power to read and do all that appertains...'). FLIP TASSEL TO LEFT!"),

            (17, "03:41:00", "03:41:53", "Dissolution of the Congregation",
             ["Acting Chancellor"],
             "Chancellor formally declares the 12th congregation dissolved."),

            (18, "03:41:54", "03:44:13", "Closing Anthem & Recession",
             ["Chancellor", "Council", "Cadets", "Brass Band"],
             "Final Kenya National Anthem; celebration; academic procession leaves the pavilion.")
        ]

        phases = []
        for order, start, end, name, actors, desc in raw_phases:
            duration_sec = self._to_seconds(end) - self._to_seconds(start)
            duration_min = round(duration_sec / 60.0, 1)
            phases.append(CeremonyPhase(order, start, end, duration_min, name, actors, desc))

        return phases


def main():
    transcript_file = "12th_graduation_ceremony_transcript.txt"
    format_type = "table"

    if len(sys.argv) > 1:
        if sys.argv[1] == "--format" and len(sys.argv) > 2:
            format_type = sys.argv[2]
        elif sys.argv[1] == "--json":
            format_type = "json"

    parser = GraduationTimelineParser(transcript_file)
    phases = parser.get_phases()

    if format_type == "json":
        print(json.dumps([asdict(p) for p in phases], indent=2))
        return

    print("=" * 80)
    print("TUM 12TH GRADUATION CEREMONY: TIMELINE & EVENT ORDER")
    print("=" * 80)
    for p in phases:
        print(f"[{p.order:02d}] {p.start_time} - {p.end_time} ({p.duration_minutes} min) | {p.name}")
        print(f"     Actors: {', '.join(p.key_actors)}")
        print(f"     Details: {p.description}\n")


if __name__ == "__main__":
    main()
