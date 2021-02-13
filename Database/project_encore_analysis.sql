-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: prospect_encore_analysis
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `userName` varchar(45) NOT NULL,
  `userPass` text,
  `userType` text,
  `fullName` text,
  `phone` text,
  `email` text,
  `status` text,
  PRIMARY KEY (`userName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('E101','password','admin','Speed','9910255122','sniperneverfails@gmail.com','activated'),('E102','sniperspeed','monitor','Sniper','99102551492','Spd12996@gmail.com','deactivated'),('E103','mona@29','admin','vikas','9910255123','vikas@gmail.com','deactivated'),('E104','monika','monitor','Monika Garg','9910255111','mona@gmail.com','activated'),('E105','pass','admin','Kuldeep','9865452341','kdeep@gmail.com','activated');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prospect`
--

DROP TABLE IF EXISTS `prospect`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prospect` (
  `prospId` int NOT NULL AUTO_INCREMENT,
  `prospName` varchar(45) DEFAULT NULL,
  `prospPhone` varchar(45) DEFAULT NULL,
  `prospAddress` varchar(45) DEFAULT NULL,
  `interestedModel` varchar(45) DEFAULT NULL,
  `interestedColor` varchar(45) DEFAULT NULL,
  `dateOfVisit` varchar(20) DEFAULT NULL,
  `priority` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`prospId`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prospect`
--

LOCK TABLES `prospect` WRITE;
/*!40000 ALTER TABLE `prospect` DISABLE KEYS */;
INSERT INTO `prospect` VALUES (1,'Sanjeev','9910255122','Delhi','Tesla Model 3','Black','2021-02-01','High'),(2,'Vikas','9852647315','Faridabad','Audi X8','Red','2021-01-01','Medium'),(3,'Ratna','9654782135','Delhi','Jaguar','Black','2021-02-03','High');
/*!40000 ALTER TABLE `prospect` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-13 22:05:56
