FROM python:3
COPY . ./
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python3", "./Test_phase.py" ]
