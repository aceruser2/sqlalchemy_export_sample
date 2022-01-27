FROM postgres:14
RUN sed -i -e 's/# zh_TW.UTF-8 UTF-8/zh_TW.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG zh_TW.UTF-8  
ENV LANGUAGE zh_TW:UTF-8  
ENV LC_ALL zh_TW.UTF-8
