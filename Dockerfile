FROM python:3
WORKDIR /usr/local/bin
COPY Test_phase.py .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["Test_phase.py"]
