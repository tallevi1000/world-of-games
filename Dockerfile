FROM python:3

RUN pip instsall Flask
ADD Test_phase.py
CMD [ "python", "./Test_phase.py" ]
