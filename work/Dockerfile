# 使用官方的 OpenJDK 17 作为基础镜像
FROM openjdk:17

# 创建应用目录
#VOLUME /tmp

# 设置环境变量
#ENV SPRING_PROFILES_ACTIVE=pro

# 复制 JAR 文件到容器中
COPY demo-maxmind-1.0-SNAPSHOT.jar demo-maxmind-1.0-SNAPSHOT.jar

# 暴露应用运行的端口
EXPOSE 9010

# 运行 JAR 文件并指定配置文件
ENTRYPOINT ["java","-jar","/demo-maxmind-1.0-SNAPSHOT.jar"]