#NOTE: DOCKER doesn't support in-line comments

# the base image for the Docker container
FROM python:3.9 


RUN pip install pandas

# set the working directory inside the container
WORKDIR /app 

# copy the pipeline script into the container, we keep the pipeline.py name as it is in the container
COPY pipeline.py /app/pipeline.py 

# This works too, as the working directory is set to /app so you don't need to specify it again
# but it's clearer to specify the full path
# so that it is clear where the file is being copied to
# If you don't specify the full path, it will copy to the current working directory
# which is /app in this case
# COPY pipeline.py pipeline.py 

ENTRYPOINT ["bash"]