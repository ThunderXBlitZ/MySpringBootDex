---
title: "@ComponentScan"
layout: mydefault
parent: "@Annotations"
---


### About

Placed on the main class of a Spring Boot application. 

### Details

A convenient shortcut annotation that encapsulates several other annotations.

- `@Configuration`: indicates the class is a source of bean definitions.

- `@EnableAutoConfiguration`: automatically configure your Spring application based on the dependencies and other configuration settings

- `@ComponentScan`: scan and discover other Spring components/beans in the specified package(s).

### Example

```
package helloworld;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MyApplication {

  public static void main(String... args) {
    SpringApplication.run(MyApplication.class, args);
  }
}
```

### Resources
- Official documentation