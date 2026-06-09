import cv2
from ultralytics import YOLO

from config import *
from utils import (
    calculate_center,
    point_in_zone
)


# Modell laden

model = YOLO(MODEL_NAME)


# Kamera starten

cap = cv2.VideoCapture(0)

# Alternativ Video verwenden:
# cap = cv2.VideoCapture("videos/test_video.mp4")

violations = 0

while True:

    success, frame = cap.read()

    if not success:
        break

    results = model(frame)

    person_in_zone = False

    for result in results:

        for box in result.boxes:

            class_id = int(box.cls[0])

            # Nur Personen erkennen
            if class_id != PERSON_CLASS_ID:
                continue

            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )

            center_x, center_y = calculate_center(
                x1,
                y1,
                x2,
                y2
            )

            # Mittelpunkt anzeigen
            cv2.circle(
                frame,
                (center_x, center_y),
                5,
                GREEN,
                -1
            )

            # Bounding Box
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                GREEN,
                2
            )

            cv2.putText(
                frame,
                "Person",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                GREEN,
                2
            )

            # Sicherheitszone prüfen
            if point_in_zone(
                center_x,
                center_y,
                ZONE_X1,
                ZONE_Y1,
                ZONE_X2,
                ZONE_Y2
            ):
                person_in_zone = True

    # ---------------------------------
    # Sicherheitszone zeichnen
    # ---------------------------------

    if person_in_zone:

        violations += 1

        zone_color = RED

        cv2.putText(
            frame,
            "WARNING: PERSON IN SAFETY ZONE",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            RED,
            3
        )

    else:
        zone_color = GREEN

    cv2.rectangle(
        frame,
        (ZONE_X1, ZONE_Y1),
        (ZONE_X2, ZONE_Y2),
        zone_color,
        3
    )

    # Verstöße anzeigen
    cv2.putText(
        frame,
        f"Violations: {violations}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        WHITE,
        2
    )

    cv2.imshow(
        WINDOW_NAME,
        frame
    )

    key = cv2.waitKey(1)

    if key == ord("q"):
        break


# Aufräumen

cap.release()
cv2.destroyAllWindows()