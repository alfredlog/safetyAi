# AI Safety Zone Monitoring System

## Overview

This project demonstrates a computer vision based safety monitoring system using YOLOv8 and OpenCV.

The system detects people in real time and monitors whether they enter a predefined safety zone. If a person enters the restricted area, the system generates a warning and records a violation event.

## Technologies

* Python
* YOLOv8
* OpenCV
* NumPy

## Features

* Real-time person detection
* Safety zone monitoring
* Visual warning system
* Violation counter
* Webcam support
* Video file support

## Motivation

Industrial environments often contain hazardous areas around machines, robots or electrical equipment.

Computer vision systems can improve workplace safety by automatically detecting workers and generating warnings when safety rules are violated.

This project demonstrates a simplified version of such a system.

## How It Works

1. YOLOv8 detects people in each frame.
2. The center point of each detected person is calculated.
3. The system checks whether the center point is inside the safety zone.
4. If a violation occurs:

   * The safety zone becomes red.
   * A warning message is displayed.
   * The violation counter increases.

## Future Improvements

* Hard hat detection
* Safety vest detection
* Multi-camera monitoring
* Person tracking
* Dashboard for analytics
* Logging to database

## Skills Demonstrated

* Computer Vision
* Deep Learning
* CNN-based Object Detection
* OpenCV
* Python Development
* AI for Workplace Safety
