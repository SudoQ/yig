#!/bin/bash
python main.py && wkhtmltopdf invoice.html out.pdf && evince out.pdf && rm invoice.html out.pdf
