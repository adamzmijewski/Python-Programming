-- MySQL dump 10.13  Distrib 8.0.15, for macos10.14 (x86_64)
--
-- Host: localhost    Database: kiosk
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `route`
--

DROP TABLE IF EXISTS `route`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `route` (
  `Id` int(11) DEFAULT NULL,
  `route_number` varchar(45) NOT NULL,
  `passengers` varchar(45) NOT NULL,
  `starting_point` varchar(45) NOT NULL,
  `end_point` varchar(45) NOT NULL,
  `time` varchar(45) NOT NULL,
  `duration` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `route`
--

LOCK TABLES `route` WRITE;
/*!40000 ALTER TABLE `route` DISABLE KEYS */;
INSERT INTO `route` VALUES (1,'dfasfd','dfasfd','dfasfd','dfasfd','dfasfd','dfasfd'),(1,'asdaf','faf','34','afafs','fafddfas','ffasd'),(1,'asdaf','faf','34','afafs','fafddfas','ffasd'),(1,'dda','ada','ada','ada','ad','asd'),(97,'r2','23','detroit','adam street','5:00pm','3 hours'),(2,'akfd','24','detroit','lansing','5:00pm','3 hours'),(4,'r3','21','warren avenue','woordward','7:00pm','2 hours'),(5,'r3','20','jewell','adams street','5:30pm','3 hours'),(7,'r13','19','jewell','chicago','5:30pm','5 hours'),(8,'r4','18','van dyke','mound','5:30pm','1 hour'),(9,'r16','18','hall road','rochester road','2:30pm','1 hour'),(10,'r4','14','hayes','romeo plank','1:30pm','2 hours');
/*!40000 ALTER TABLE `route` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tickets`
--

DROP TABLE IF EXISTS `tickets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tickets` (
  `code` varchar(45) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `depart_time` varchar(45) DEFAULT NULL,
  `arrive_time` varchar(45) DEFAULT NULL,
  `startpoint` varchar(45) DEFAULT NULL,
  `endpoint` varchar(45) DEFAULT NULL,
  `seat_num` varchar(45) DEFAULT NULL,
  `depart_date` varchar(45) DEFAULT NULL,
  `arrival_date` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tickets`
--

LOCK TABLES `tickets` WRITE;
/*!40000 ALTER TABLE `tickets` DISABLE KEYS */;
INSERT INTO `tickets` VALUES ('0000reeee1','adam','zmijewsi','8:39pm',NULL,'go to richard selection',NULL,NULL,'2/22/2//',NULL),('1','',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('111','adam','zmijewski','fh3oj23',NULL,'kdnknsakdn',NULL,NULL,'smalsmalm',NULL),('1234r1','adam','zmijewski','fh7020','8:59pm','Adams street','Woodward','23b','2/2/13','2/3/4'),('1234r2','jeffrey','zmijewski','fh7020','8:59pm','Adams street','Woodward','23b','2/2/13','2/3/4');
/*!40000 ALTER TABLE `tickets` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-06 21:29:36
