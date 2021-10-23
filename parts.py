from mysql.connector import Error
from conn_db import Database

from PyQt5.QtWidgets import *

import ui.p_add_ui


class Part:
    def __init__(self, name, price, brand, p_id=None):
        self.part_id = p_id
        self.name = name
        self.price = price
        self.brand = brand

    def add(self):
        conn = Database()
        sql = "INSERT INTO parts(part_name, part_price, brand) VALUES(%s, %s, %s)"
        values = (self.name, self.price, self.brand)
        try:
            conn.cursor.execute(sql, values)
            conn.connection.commit()
        except Error as e:
            print(e)
        finally:conn.close()

    def part_update(self):
        conn = Database()
        sql = "UPDATE parts " \
              "SET part_name=%s, part_price=%s, brand=%s " \
              "WHERE part_id=%s"
        values = (self.name, self.price, self.brand, self.part_id)
        try:
            conn.cursor.execute(sql, values)
            conn.connection.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

    @staticmethod
    def part_delete(p_id):
        conn = Database()
        deleted = False
        try:
            print("part del ")
            conn.cursor.execute("DELETE FROM parts "
                                "WHERE part_id = %s", (p_id,))
            conn.connection.commit()
            deleted = True
        except Error as e:
            conn.connection.rollback()
            print(e)
        finally:
            conn.close()
            return deleted

    @staticmethod
    def part_search(p_id):
        conn = Database()
        try:
            conn.cursor.execute("SELECT * FROM parts "
                                "WHERE part_id=%s", (p_id,))
            result = conn.cursor.fetchone()
            return result
        except Error as e:
            print(e)
        finally:
            conn.close()

    @staticmethod
    def view():
        conn = Database()
        try:
            conn.cursor.execute("SELECT * FROM parts")
            result = conn.cursor.fetchall()
            return result
        except Error as e:
            print(e)
        finally:
            conn.close()


class PartUI(QDialog, ui.p_add_ui.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.show()
        self.bt_cancel.clicked.connect(self.close)

    def part_ui_add(self):
        print("add ui started")
        self.name = self.input_p_name.text()
        self.price = self.input_p_price.text()
        self.brand = self.input_p_brand.text()
        part_obj = Part(self.name, self.price, self.brand)
        part_obj.add()
        self.close()

    def part_ui_update(self):
        p_id = self.input_p_id.text()
        p_name = self.input_p_name.text()
        brand = self.input_p_brand.text()
        price = self.input_p_price.text()
        part_obj = Part(p_name, price, brand, p_id=p_id)
        part_obj.part_update()
        self.close()