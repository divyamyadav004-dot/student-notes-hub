#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PDF_ROOT = ROOT / "assets" / "pdfs"

CORE_NOTES = {
    "class9": {
        "label": "Class 9",
        "subjects": {
            "Physics": ["Motion and Laws", "Work and Energy", "Gravitation"],
            "Chemistry": ["Matter in Our Surroundings", "Atoms and Molecules", "Is Matter Around Us Pure"],
            "Maths": ["Number Systems", "Polynomials", "Coordinate Geometry"],
        },
    },
    "class10": {
        "label": "Class 10",
        "subjects": {
            "Physics": ["Motion and Laws", "Work, Energy and Power", "Current Electricity"],
            "Chemistry": ["Structure of Atom", "Chemical Reactions", "Organic Basics"],
            "Maths": ["Quadratic Equations", "Trigonometry", "Probability"],
        },
    },
    "class11": {
        "label": "Class 11",
        "subjects": {
            "Physics": ["Units and Measurements", "Kinematics", "Laws of Motion"],
            "Chemistry": ["Some Basic Concepts of Chemistry", "Structure of Atom", "Chemical Bonding"],
            "Maths": ["Sets and Functions", "Trigonometric Functions", "Straight Lines"],
            "Biology": ["The Living World", "Plant Kingdom", "Cell Structure and Function"],
        },
    },
    "class12": {
        "label": "Class 12",
        "subjects": {
            "Physics": ["Electrostatics", "Current Electricity", "Ray Optics"],
            "Chemistry": ["Solutions", "Electrochemistry", "Haloalkanes and Haloarenes"],
            "Maths": ["Relations and Functions", "Matrices", "Differential Equations"],
            "Biology": ["Reproduction in Organisms", "Genetics and Evolution", "Biotechnology"],
        },
    },
    "jee": {
        "label": "JEE",
        "subjects": {
            "Physics": ["Kinematics", "Laws of Motion", "Electrostatics", "Modern Physics"],
            "Chemistry": ["Mole Concept", "Chemical Bonding", "Thermodynamics", "Organic Reaction Mechanisms"],
            "Maths": ["Limits and Continuity", "Matrices", "Differential Equations", "Probability"],
        },
    },
    "neet": {
        "label": "NEET",
        "subjects": {
            "Physics": ["Kinematics", "Laws of Motion", "Current Electricity", "Semiconductors"],
            "Chemistry": ["Atomic Structure", "Chemical Bonding", "Thermodynamics", "Biomolecules"],
            "Biology": ["Cell Biology", "Genetics", "Human Physiology", "Ecology"],
        },
    },
}

EXTRA_PDFS = [
    ("class10", "PYQ", "2025 Class 10 Board PYQs", "class10-board-pyq-2025.pdf"),
    ("class10", "PYQ", "2024 Class 10 Board PYQs", "class10-board-pyq-2024.pdf"),
    ("class10", "PYQ", "2023 Class 10 Board PYQs", "class10-board-pyq-2023.pdf"),
    ("class10", "PYQ", "2022 Class 10 Board PYQs", "class10-board-pyq-2022.pdf"),
    ("class10", "PYQ", "2021 Class 10 Board PYQs", "class10-board-pyq-2021.pdf"),
    ("class12", "PYQ", "2025 Class 12 Board PYQs", "class12-board-pyq-2025.pdf"),
    ("class12", "PYQ", "2024 Class 12 Board PYQs", "class12-board-pyq-2024.pdf"),
    ("class12", "PYQ", "2023 Class 12 Board PYQs", "class12-board-pyq-2023.pdf"),
    ("class12", "PYQ", "2022 Class 12 Board PYQs", "class12-board-pyq-2022.pdf"),
    ("class12", "PYQ", "2021 Class 12 Board PYQs", "class12-board-pyq-2021.pdf"),
    ("jee", "PYQ", "2025 JEE PYQs", "jee-pyq-2025.pdf"),
    ("jee", "PYQ", "2024 JEE PYQs", "jee-pyq-2024.pdf"),
    ("jee", "PYQ", "2023 JEE PYQs", "jee-pyq-2023.pdf"),
    ("jee", "PYQ", "2022 JEE PYQs", "jee-pyq-2022.pdf"),
    ("jee", "PYQ", "2021 JEE PYQs", "jee-pyq-2021.pdf"),
    ("neet", "PYQ", "2025 NEET PYQs", "neet-pyq-2025.pdf"),
    ("neet", "PYQ", "2024 NEET PYQs", "neet-pyq-2024.pdf"),
    ("neet", "PYQ", "2023 NEET PYQs", "neet-pyq-2023.pdf"),
    ("neet", "PYQ", "2022 NEET PYQs", "neet-pyq-2022.pdf"),
    ("neet", "PYQ", "2021 NEET PYQs", "neet-pyq-2021.pdf"),
    ("class9", "Syllabus", "Science and Maths Syllabus Board", "science-maths-syllabus-board.pdf"),
    ("class10", "Syllabus", "Social Science Syllabus", "social-science-syllabus.pdf"),
    ("class11", "Syllabus", "Physics Chemistry Maths Stream", "pcm-stream-syllabus.pdf"),
    ("class12", "Syllabus", "Physics Chemistry Biology Stream", "pcb-stream-syllabus.pdf"),
    ("jee", "Syllabus", "JEE Main Official Syllabus", "jee-main-syllabus.pdf"),
    ("jee", "Syllabus", "JEE Advanced Topic Breakdown", "jee-advanced-topic-breakdown.pdf"),
    ("neet", "Syllabus", "NEET Official Syllabus", "neet-official-syllabus.pdf"),
    ("neet", "Syllabus", "Unit wise NEET Outline", "neet-unit-wise-outline.pdf"),
]


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value


def escape_pdf_text(value: str) -> str:
    return value.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def build_pdf(text: str) -> bytes:
    stream = f"BT /F1 18 Tf 72 740 Td ({escape_pdf_text(text)}) Tj ET"
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>",
        f"<< /Length {len(stream.encode('latin-1'))} >>\nstream\n{stream}\nendstream".encode("latin-1"),
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
    ]

    output = bytearray(b"%PDF-1.4\n")
    offsets = [0]

    for index, obj in enumerate(objects, start=1):
        offsets.append(len(output))
        output.extend(f"{index} 0 obj\n".encode("ascii"))
        output.extend(obj)
        output.extend(b"\nendobj\n")

    xref_start = len(output)
    output.extend(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
    output.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        output.extend(f"{offset:010d} 00000 n \n".encode("ascii"))

    output.extend(
        f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref_start}\n%%EOF\n".encode(
            "ascii"
        )
    )
    return bytes(output)


def write_pdf(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(build_pdf(text))


def generate_core_notes() -> int:
    created = 0
    for folder, details in CORE_NOTES.items():
        class_label = details["label"]
        for subject, chapters in details["subjects"].items():
            subject_slug = slugify(subject)
            for chapter in chapters:
                filename = f"{subject_slug}-{slugify(chapter)}.pdf"
                text = f"Sample Notes - {class_label} - {subject} - {chapter}"
                write_pdf(PDF_ROOT / folder / filename, text)
                created += 1
    return created


def generate_extra_docs() -> int:
    created = 0
    for folder, subject, chapter, filename in EXTRA_PDFS:
        class_label = CORE_NOTES[folder]["label"]
        text = f"Sample Notes - {class_label} - {subject} - {chapter}"
        write_pdf(PDF_ROOT / folder / filename, text)
        created += 1
    return created


def main() -> None:
    created = generate_core_notes() + generate_extra_docs()
    print(f"Generated {created} placeholder PDFs in {PDF_ROOT}")


if __name__ == "__main__":
    main()
