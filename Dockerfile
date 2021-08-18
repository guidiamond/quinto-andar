FROM tensorflow/tensorflow:latest-gpu

RUN pip install --upgrade pip

RUN useradd -ms /bin/bash worker

USER worker
WORKDIR /home/worker

ENV PATH="/home/worker/.local/bin:${PATH}"

COPY --chown=worker:worker . .

RUN pip install --user -r requirements.txt

CMD ["python", "train.py"]
