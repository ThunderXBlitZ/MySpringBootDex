---
title: "Create Project"
layout: mydefault
parent: Beginner
tags:
- beginner
- springboot
---

### About

Visit [Spring Initializr](https://start.spring.io/) to generate your boilerplate source code

![Spring Initializr UI]({{site.baseurl}}/assets/images/docs/beginner/create_project/spring_initializr.png)

Make sure you have a suitable version of [JDK](https://www.oracle.com/sg/java/technologies/downloads/) installed e.g. 22

<br>

### Details

#### Part 1:

1. Fill in the project details:
```
Project: Maven // we use Maven as our Build Tool
Language: Java
Spring Boot: Choose the latest stable version
Group: com.example (you can choose any name)
Artifact: my-spring-boot-app (you can choose any name)
```

2. Choose the Java version you have installed.

3. Leave other options as default.

4. Click “Generate” to download the starter project as a zip file.

<br>

> Note:
> 
> - Notice the option "Jar vs War". Spring Boot .jar file is an executable that will contain all the required > dependencies and an embedded web server (e.g. Tomcat), that makes it easy to package and deploy.
> Spring Boot .war file requires an existing web server to run, which may be useful if you have multiple web apps to run together.
> 
> - Notice the section 'Dependencies' on the right, you may add required dependencies e.g. Spring Security in the future. The dependency modules provide various powerful, battle-tested boilerplate code for setting up a web application, security practices, dev tools, which is one of the key strengths of the Spring Ecosystem.

![Spring Dependencies UI]({{site.baseurl}}/assets/images/docs/beginner/create_project/spring_dependencies.png)

<br>

#### Part 2:
1. Unzip the downloaded zip file.

2. You’ll find a basic Spring Boot project structure.

3. Open the project in your favorite text editor or IDE (e.g., IntelliJ IDEA, Eclipse, Visual Studio Code).

4. Verify that the source code contains DemoApplication.javam typically under `/src/main/java/<your package>`

5. Run the project (you may need to setup additional configurations for your IDE)

<br>

### Output
The project should successfully terminate with a log similar to:
```
com.example.demo.DemoApplication         : Started DemoApplication in 0.757 seconds
```

Congrats! You have successfully ran your first Spring Boot project. Of course it doesn't do anything yet, but pat yourself on the back for taking the first step!

<br>

### Resources
- [Official Spring documentation](https://docs.spring.io/spring-framework/reference/index.html)
- [Official SpringBoot documentation](https://spring.io/projects/spring-boot)