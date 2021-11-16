-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema service_management
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema service_management
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `service_management` DEFAULT CHARACTER SET utf8 ;
USE `service_management` ;

-- -----------------------------------------------------
-- Table `service_management`.`Customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `service_management`.`Customer` (
  `customer_id` INT NOT NULL AUTO_INCREMENT,
  `customer_name` VARCHAR(45) NOT NULL,
  `address` VARCHAR(150) NULL,
  `contact_no` BIGINT(10) UNSIGNED NULL,
  `email` VARCHAR(80) NULL,
  PRIMARY KEY (`customer_id`),
  UNIQUE INDEX `contact_no_UNIQUE` (`contact_no` ASC) INVISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `service_management`.`Vehicle`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `service_management`.`Vehicle` (
  `vehicle_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `registration_no` VARCHAR(10) NOT NULL,
  `company` VARCHAR(45) NOT NULL,
  `model` VARCHAR(45) NOT NULL,
  `vehicle_type` VARCHAR(20) NULL,
  `transmission` ENUM('automatic', 'manual') NULL,
  `customer_id` INT NOT NULL,
  PRIMARY KEY (`vehicle_id`),
  UNIQUE INDEX `registration_no_UNIQUE` (`registration_no` ASC) VISIBLE,
  INDEX `FK_OWNER_idx` (`customer_id` ASC) VISIBLE,
  CONSTRAINT `FK_OWNER`
    FOREIGN KEY (`customer_id`)
    REFERENCES `service_management`.`Customer` (`customer_id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `service_management`.`Employee`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `service_management`.`Employee` (
  `employee_id` INT NOT NULL AUTO_INCREMENT,
  `employee_name` VARCHAR(45) NOT NULL,
  `employee_address` VARCHAR(150) NULL,
  `employee_contact_no` BIGINT(10) NULL,
  `date_of_joining` DATE NOT NULL,
  `salary` INT NULL,
  PRIMARY KEY (`employee_id`),
  UNIQUE INDEX `employee_contact_no_UNIQUE` (`employee_contact_no` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `service_management`.`Service`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `service_management`.`Service` (
  `service_id` INT NOT NULL AUTO_INCREMENT,
  `description` TINYTEXT NULL,
  `service_date` DATE NOT NULL,
  `kilometer` INT UNSIGNED NULL,
  `damages` VARCHAR(45) NULL,
  `total_price` FLOAT NOT NULL,
  `vehicle_id` INT UNSIGNED NULL,
  `employee_id` INT NULL,
  PRIMARY KEY (`service_id`),
  INDEX `FK_VEHICLE_idx` (`vehicle_id` ASC) VISIBLE,
  INDEX `FK_EMPLOYEE_idx` (`employee_id` ASC) VISIBLE,
  CONSTRAINT `FK_VEHICLE`
    FOREIGN KEY (`vehicle_id`)
    REFERENCES `service_management`.`Vehicle` (`vehicle_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_EMPLOYEE`
    FOREIGN KEY (`employee_id`)
    REFERENCES `service_management`.`Employee` (`employee_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = '		';


-- -----------------------------------------------------
-- Table `service_management`.`Parts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `service_management`.`Parts` (
  `part_id` INT NOT NULL,
  `part_name` VARCHAR(60) NOT NULL,
  `part_price` FLOAT UNSIGNED NOT NULL,
  `brand` VARCHAR(45) NULL,
  PRIMARY KEY (`part_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `service_management`.`Parts_Used`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `service_management`.`Parts_Used` (
  `Service_service_id` INT NOT NULL,
  `Parts_part_id` INT NOT NULL,
  `quantity` TINYINT(3) NULL,
  PRIMARY KEY (`Service_service_id`, `Parts_part_id`),
  INDEX `FK_PARTS_USED_PARTS` (`Parts_part_id` ASC) INVISIBLE,
  INDEX `FK_PARTS_USED_SERVICE` (`Service_service_id` ASC) VISIBLE,
  CONSTRAINT `FK_PARTS_USED_SERVICE`
    FOREIGN KEY (`Service_service_id`)
    REFERENCES `service_management`.`Service` (`service_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `FK_PARTS_USED_PARTS`
    FOREIGN KEY (`Parts_part_id`)
    REFERENCES `service_management`.`Parts` (`part_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
