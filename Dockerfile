FROM python:3
COPY Test_phase.py Scores.txt ./
# RUN pip install --no-cache-dir -r requirements.txt
CMD ["Test_phase.py"]
EXPOSE 8777/tcp
