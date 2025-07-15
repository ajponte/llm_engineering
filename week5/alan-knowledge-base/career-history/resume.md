Alan J. Ponte
Phone: 510.303.3352
LinkedIn: https://www.linkedin.com/in/alan-jason-ponte/
Email: alanjponte@gmail.com
Github: https://github.com/ajponte

EMPLOYMENT


Tech Lead – Web Services                                      AndGo by Goodyear                                        April 2022 – Current
	Lead the backend development of a distributed micro-services architecture across cross-functional agile teams.
	Mentor engineers on software engineering best practices and hold regular 1-1 meetings.
	Regularly contribute to engineering roadmap planning and product strategy.
Notable Projects
•	Dynamic Appointment Scheduler (Python/Flask, AWS RDS, Elasticache, SNS, SQS, Docker, K8s). I was an architect and lead developer for this project. The output of the application was suggested service times for Fleet Managers to schedule vehicle maintenance at various Goodyear service centers. The system evolved through two major iterations, where the first iteration was essentially a monolithic application, and the second iteration was asynchronous and event driven. In the second iteration, I segregated the system by the domain of finding available service times, and the domain of scheduling the service. The results of service time calculations temporarily persisted in a Redis sorted set, to utilize the O(lgN) expected runtime of the zrangebyscore operation.

•	Geotab Data Lake Integration (Python/Flask, AWS RDS, S3, Docker, K8s). I was an architect and lead developer for this project. Geotab is an OBD device installed on specific vehicles to aggregate telematics. An API endpoint on the integration service (which I had bult previously for aggregating odometer data for a specific fleet) to fetch data via the Geotab API at regular intervals, which was triggered by a CronJob. Once the data was fetched, it was pushed to a data lake (S3 bucket). I designed a Python application, which continuously ran in a docker container to scan the S3 bucket for new data at regular intervals, and updated vehicle telematics upon changes.

•	Notification Service (Python/Flask, AWS, RDS, Docker, K8s). I was an architect and lead developer for this project. This service supported 3 notification channels (SMS, Email, In-App) as well as call-to-actions. I also developed a templating system for future extensibility.

Technical Project Lead (Contract)                       Vitalyze Inc.			               May 2021 - August 2021
	Lead a small team on the effort to implement agile software development practices.
	Coordinated with internal sales department and data providers as technical point of contact for onboarding.
	Created project planning artifacts such as roadmaps and technical requirements documents.
	Lead the effort to integrate a new partner onto the existing Pharmacy Rebate platform.
	Created a Kanban workflow for existing business rules.
	Created a scrum workflow for new feature development.

Software Engineer                                                  Location Labs by Avast                                August 2015 - January 2021
	Design, implement, and test backend features, REST APIs, and bug-fixes in a data-driven, service-oriented/microservices architecture, primarily using Java-Spring and Python-Flask.
	Contribute to code and design reviews.
	Coordinate with business stakeholders as a technical point of contact for product and project roadmaps.
	Manage end of sprint releases.
	Coordinate with Customer Support, Network Operations, and relevant stakeholders to find RCAs for incidents and outages.
	Scrum master rotation responsibilities, including leading daily stand-ups and sprint planning meetings.
Notable Projects
•	AT&T Subscription Service (Java/Spring, Redis, MySQL, Docker). I was an individual contributor for this project. The goal was to develop a system which would keep AT&T family plan subscriptions in-sync with Location Lab subscriptions. The subscription model allowed Location Labs to bill customers based on desired plans. I implemented a cache-aside strategy in Redis to reduce latency of fetching subscription operations.

•	Verizon CCPA Pipeline (Python/Flask, MySQL, AWS SQS/SNS, Docker, K8s). I was an individual contributor on this project. The goal was to develop a pipeline to support CCPA compliance for Verizon products. The solution included an HTTP server, a producer, and a consumer application. I designed and implemented the base consumer which required integration with every microservice and database which supported Verizon features.

Contractor (part-time)                                            Alkyme		                                           December 2014 - March 2015
	Supported the full stack development of a web portal between patients and physicians, using the M.E.A.N. stack (MongoDB, Express, AngularJS, NodeJS).

Computer Systems Engineer          Lawrence Berkeley National Laboratory                         December 2013 - August 2015
	Created and maintained tools and applications to facilitate the operational duties of laboratory staff.
	Supported system and server upgrades.
	Managed account setup for new users.
Notable Projects
•	ABPDU Web App (AngularJS, NodeJS, MongoDB, Google App Engine). I was an individual contributor on this project. The goal was to develop a web application to enable inter/intra-lab communication between various research groups. The web application allowed researchers to upload experiment data to a platform to depreciate an old system of faxing documents. I worked on every layer of the stack to implement a set of CRUD endpoints.
•	Gmail Migration (Bash script, Google Apps Script). I was an individual contributor on this project. The goal was to develop a set of scripts to migrate email data from in-house SMTP/IMAP servers and clients to Gmail. I coordinated with laboratory staff to ensure all their desired email data was successfully transferred and helped with bug fixing where appropriate.

EDUCATION
Berkeley, CA                                       University of California, Berkeley                                   December 2013
	B.A. in Applied Mathematics, concentration in economics.

TECHNICAL SKILLS
	Languages: Python, Java, JavaScript, Bash Scrpting, Lisp, Clojure, Matlab

	Tools & Frameworks: Flask, Spring, MySQL, Postgres, Docker, AWS (SQS, SNS, RDS, S3), Terraform, Kubernetes, Spinnaker, Redis, Swagger, Ansible, Loggly, Datadog, Apache Tomcat, Nagios, NodeJS, AngularJS, MongoDB, Pandas, GraphQL, Hasura.
