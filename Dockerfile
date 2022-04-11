FROM sandy1709/catuserbot:alpine

#clonning repo 
RUN git clone https://github.com/KillerXaman/KillerXspam.git /root/KillerXspam
#working directory 
WORKDIR /root/KillerXspam

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/KillerXspam/bin:$PATH"

CMD ["python3","-m","KillerXspam"]
