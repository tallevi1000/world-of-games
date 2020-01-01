FROM python:3
COPY Test_phase.py .
# RUN pip install --no-cache-dir -r requirements.txt
CMD ["Test_phase.py"]
