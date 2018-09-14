"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: b_NewOrder.py
@time: 2018/9/7 17:23
@desc: ���б���������ҵ���߼�����
"""
from elements.el_JYT.el_NewOrder_1 import C_el_NewOrder_1
from elements.el_JYT.el_NewOrder_2 import C_el_NewOrder_2
from elements.el_JYT.el_NewOrder_3 import C_el_NewOrder_3
from elements.el_JYT.el_NewOrder_4 import C_el_NewOrder_4
from elements.el_JYT.el_NewOrder_5 import C_el_NewOrder_5
from common.rewrite import C_selenium_rewrite
import unittest
import time
from selenium.webdriver.common.touch_actions import TouchActions
class C_B_NewOrder(unittest.TestCase):

    def setUp(self):
        self.Cel_NewOrder_1 = C_el_NewOrder_1()  #ʵ����
        self.Cel_NewOrder_2 = C_el_NewOrder_2()
        self.Cel_NewOrder_3 = C_el_NewOrder_3()
        self.Cel_NewOrder_4 = C_el_NewOrder_4()
        self.Cel_NewOrder_5 = C_el_NewOrder_5()
        self.C_sel_Rewrite  = C_selenium_rewrite()
        self.TouchAct = TouchActions()
        self.shopName = u"ѡ����Ʒ�ŵ�"
        self.goodType = u"ѡ����Ʒ����"
        self.productVersion = u"ѡ���Ʒ�汾"
        self.productType = u"ѡ���Ʒ���"
        self.lName = ['42010000200 - �人�н��������ͨѶ���ľ�Ӫ��', '�ֻ�', '������B', '����']  #��ȡExcel����


    def b_Choose_Shop_Click(self, driver):
        """
        ����ŵ꣬��������
        :param driver:
        :param shopeName:��Ʒ�ŵ�����
        :return:
        """
        self.Cel_NewOrder_1.el_NewOrder1_ChooseBaseInfo_PopUP(driver, 1)  #�����Ʒ�ŵ�

    def b_Common_Choose(self, driver, tName, strName):
        #����ѡ�����ݹ�������
        #�ĸ����͵ĵ���������һ��list���棬�����β�
        if self.Cel_NewOrder_1.el_NewOrder_Common_PopUp_Title(driver).getText().strip() == tName:
            self.Cel_NewOrder_1.el_NewOrder_Common_PopUp_List(driver, strName).click()
        else:
            print("����ѡ�� %s ����" % strName)

    def b_Chose_GoodsType_Click(self, driver):
        """
        �����Ʒ���� ����
        :param driver:
        :param GoodsType: ��Ʒ����
        :return:
        """
        self.Cel_NewOrder_1.el_NewOrder1_ChooseBaseInfo_PopUP(driver, 2)  # �����Ʒ����

    def b_Choose_ProductVerson_Click(self, driver):
        """
        ѡ���Ʒ�汾
        :param driver:
        :param ProductVerson: ��Ʒ�汾
        :return:
        """
        self.Cel_NewOrder_1.el_NewOrder1_ChooseBaseInfo_PopUP(driver, 3)  # �����Ʒ�汾
        # ���ﻹûдѡ���Ʒ�汾����

    def b_Choose_ProductType_Click(self, driver):
        """
        ѡ���Ʒ����
        :param driver:
        :param ProductType: ��Ʒ����
        :return:
        """
        self.Cel_NewOrder_1.el_NewOrder1_ChooseBaseInfo_PopUP(driver, 4)  # �����Ʒ����
        # ���ﻹûдѡ���Ʒ���ʹ���

    def b_Fill_GoodsTotel(self, driver, GoodsTotel):
        """
        ��д��Ʒ�ܶ�
        :param driver:
        :param GoodsTotel: ��Ʒ�ܶ�
        :return:
        """
        self.Cel_NewOrder_1.el_NewOrder1_MoneyTotle(driver, 1).clear()
        self.Cel_NewOrder_1.el_NewOrder1_MoneyTotle(driver, 1).send_keys(GoodsTotel)

    def b_Fill_Downpayment(self, driver, Downpayment):
        """
        ��д�׸����
        :param driver:
        :param Downpayment: �׸����
        :return:
        """
        self.Cel_NewOrder_1.el_NewOrder1_MoneyTotle(driver, 2).clear()
        self.Cel_NewOrder_1.el_NewOrder1_MoneyTotle(driver, 2).send_keys(Downpayment)


    # -------------------------------------------------------------
    """ҵ�����"""
    # -------------------------------------------------------------
    def b_NewOrder_1(self, driver, goodsTotel, downpayment):
        """
        �½���������һ��������дҳ�棬����
        :goodsTotel:��Ʒ�ܼ�
        :downpayment:�׸��ܶ�
        :return:
        """
        self.b_Choose_Shop_Click(driver)
        self.b_Common_Choose(driver, self.shopName, self.lName[0])
        self.b_Chose_GoodsType_Click(driver)
        self.b_Common_Choose(driver, self.goodType, self.lName[1])
        self.b_Choose_ProductVerson_Click(driver)
        self.b_Common_Choose(driver, self.productVersion, self.lName[2])
        self.b_Choose_ProductType_Click(driver)
        self.b_Common_Choose(driver, self.productType, self.lName[3])
        self.b_Fill_GoodsTotel(driver, goodsTotel)
        self.b_Fill_Downpayment(driver, downpayment)

    def b_NewOrder_1_submit(self, driver):
        """��һ���ύ"""
        self.Cel_NewOrder_1.el_NewOrder_submit_1(driver).click()

    def b_Check_LoanSum(self, driver, goodsTotel, downpayment):
        """
        ��֤�������Ƿ���ȷ
        :param driver:
        :param goodsTotel: ��Ʒ�ܼ�
        :param downpayment:�׸����
        :return:
        """
        loanSum = int((self.Cel_NewOrder_1.el_NewOrder1_LoanSum(driver)).strip())
        tt = int(goodsTotel) - int(downpayment)
        if tt == loanSum:
            return True
        else:
            self.assertEquals(int(goodsTotel) - int(downpayment), loanSum, u"errorInfo:��������㲻��ȷ")
            return False

    #--------------------------------------------------
    #�½������ڶ���ҳ��--------------------------------
    def b_NewOrder_2_Check_LoanSum(self, driver, loanSum):
        """���������Ƿ���ȷ"""
        sText = self.Cel_NewOrder_2.el_NewOrder2_LoanSum(driver).getText().strip()
        if sText != loanSum:
            self.assertEquals(sText, loanSum, u"�½������ڶ���ҳ�棬��������ʾ��������!")
        else:
            #������־��Ϣ
            print(u"������Ϣ��ʾ��ȷ��")

    def b_NewOrder_2_No_TreasureFee(self, driver):
        """���μ��⻹�����"""
        #ͨ���������ƶ�Ԫ�ء���ͬ�ֱ��ʣ�������bug���Ժ�����취
        driver.flick(1040, 322, 934, 322)

    def b_NewOrder_2_ChooseInstalment(self, driver, instalment):
        """ѡ�����"""
        instal = self.Cel_NewOrder_2.el_NewOrder2_InstalmentItem(driver, instalment)
        l_instals = []
        for el in instal:
            l_instals.append(el.getText().strip())
        index = 0
        if len(l_instals) == 0:
            #�������¼��־��Ϣ
            print("��ѯ������%s - %s - %s - %s : û����������Ʒ���ڣ�������ѡ�ŵ꼰��Ʒ���ͣ���Ʒ�汾���Ƿ���ȷ" % self.shopName, self.goodType, self.productVersion, self.productType)
            return
        else:
            for str in l_instals:
                if str == instalment:
                    index = l_instals.index(str)
            self.Cel_NewOrder_2.el_NewOrder2_InstalmentList(driver)[index].click()

    def b_NewOrder_2_Submit(self, driver):
        """�����һ��"""
        self.Cel_NewOrder_2.el_NewOrder2_Submit(driver).click()

    #-----------------------------------------------------------------------------
    #�½�����������
    #-----------------------------------------------------------------------------
    def b_NewOrder_3_Choose_SubCategory(self, driver, subCategory):
        """ѡ����ƷС��"""
        self.Cel_NewOrder_3.el_NewOrder3_Choose_GoodsInfo_Click(driver)[0].click()
        if self.Cel_NewOrder_3.el_NewOrder3_PopUp_Common_Title(driver).getText().strip() == u"ѡ����ƷС��":
            els = self.Cel_NewOrder_3.el_NewOrder3_PopUp_Common_Items(driver)
            for el  in els:
                if el.getText().strip() == subCategory:
                    el.click()
                else:
                    return

    def b_NewOrder_3_Check_SubCategory(self, driver, subCategory):
        """��֤�Ƿ�ɹ�ѡ����ƷС��"""
        subText = self.Cel_NewOrder_3.el_NewOrder3_Choose_GoodsInfo_Click(driver, 0).getText().strip()
        if subText == subCategory:
            print("�ɹ�ѡ����ƷС��")
        else:
            print("ѡ����ƷС��ʧ�ܣ�����")

    def b_NewOrder_3_Choose_Brand(self, driver, brand):
        """ѡ����ƷƷ��"""
        self.Cel_NewOrder_3.el_NewOrder3_Choose_GoodsInfo_Click(driver, 1).click()
        if self.Cel_NewOrder_3.el_NewOrder3_PopUp_Common_Title(driver).getText().strip() == u"ѡ����ƷƷ��":
            els = self.Cel_NewOrder_3.el_NewOrder3_PopUp_Common_Items(driver)
            for el  in els:
                if el.getText().strip() == brand:
                    el.click()
                else:
                    return

    def b_NewOrder_3_Check_brand(self, driver, brand):
        """��֤�Ƿ�ɹ�ѡ����ƷƷ��"""
        subText = self.Cel_NewOrder_3.el_NewOrder3_Choose_GoodsInfo_Click(driver, 1).getText().strip()
        if subText == brand:
            print("�ɹ�ѡ����ƷƷ��")
        else:
            print("ѡ����ƷƷ��ʧ�ܣ�����")

    def b_NewOrder_3_Choose_SKU(self, driver, sku):
        """
        ѡ����Ʒ�ͺš�PS����ʱ����������ʽ����ʱ���������ʽ��ע�⣡����
        :param driver:
        :param sku:
        :return:
        """
        #����������
        br = self.Cel_NewOrder_3.el_NewOrder3_Edit_GP_DP(driver,2).is_Displayed()
        bh = self.Cel_NewOrder_3.el_NewOrder3_Edit_GP_DP(driver,2)
        if br == True:
            self.C_sel_Rewrite.send_keys(bh, sku)
        else:
            #��������ʽ
            self.Cel_NewOrder_3.el_NewOrder3_Choose_GoodsInfo_Click(driver, 2).click()
            if self.Cel_NewOrder_3.el_NewOrder3_PopUp_Common_Title(driver).getText().strip() == u"ѡ����Ʒ�ͺ�":
                els = self.Cel_NewOrder_3.el_NewOrder3_PopUp_Common_Items(driver)
                for el in els:
                    if el.getText().strip() == sku:
                        el.click()
                    else:
                        return

    def b_NewOrder_3_Check_SKU(self, driver, sku):
        """��֤�Ƿ�ɹ�ѡ����Ʒ�ͺ�"""
        subText = self.Cel_NewOrder_3.el_NewOrder3_Choose_GoodsInfo_Click(driver, 2).getText().strip()
        if subText == sku:
            print("�ɹ�ѡ����Ʒ�ͺ�")
        else:
            print("ѡ����Ʒ�ͺ�ʧ�ܣ�����")


    #----------------------------------------------------------------------------------
    #�����������Ĳ�����д�ͻ���Ϣ

    def b_NewOrder_4_Upload_IDFront(self, driver):
        """�ϴ�����֤����"""
        #����
        self.Cel_NewOrder_4.el_NewOrder4_IDCard_Front(driver).click()
        act_Camera = "com.giveu.corder.ordercreate.activity.CameraActivity"
        driver.wait_activity(act_Camera, 20, 1)
        self.Cel_NewOrder_4.el_NewOrder4_Camera_Shot(driver).click()
        #��֤����missed

    def b_NewOrder_4_cName(self, driver, cName):
        # ��д�û�����
        hName = self.Cel_NewOrder_4.el_NewOrder4_ID_Name(driver)
        self.C_sel_Rewrite.send_keys(hName, cName)

    def b_NewOrder_4_IDNo(self, driver, idNo):
        #����֤��
        hIDNo = self.Cel_NewOrder_4.el_NewOrder4_ID_No(driver)
        self.C_sel_Rewrite.send_keys(hIDNo, idNo)

    def b_NewOrder_4_parentAddr(self, driver, l_addr):
        """
        ѡ��ʡ����,
        :param driver:
        :param l_addr: ʡ�����б�
        :return:
        """
        self.Cel_NewOrder_4.el_NewOrder4_Address_Click(driver).click()
        hAddrs = self.Cel_NewOrder_4.el_NewOrder4_Choose_Address(driver)
        for addr in hAddrs:
            #ѡ��ʡ
            if addr.getText().strip() == l_addr[0]:
                addr.click()
                #ѡ����
                hAddrs = self.Cel_NewOrder_4.el_NewOrder4_Choose_Address(driver)
                for addr in hAddrs:
                    # ѡ��ʡ
                    if addr.getText().strip() == l_addr[1]:
                        addr.click()
                        #ѡ������
                        hAddrs = self.Cel_NewOrder_4.el_NewOrder4_Choose_Address(driver)
                        for addr in hAddrs:
                            # ѡ��ʡ
                            if addr.getText().strip() == l_addr[2]:
                                addr.click()

    def b_NewOrder_4_AddressDetail(self, driver, addrDetail):
        #��д��ϸ��ַ
        hAddr = self.Cel_NewOrder_4.el_NewOrder4_ID_Address(driver)
        self.C_sel_Rewrite.send_keys(hAddr, addrDetail)

    #����֤������Ϣ---------------------------------------
    def b_NewOrder_4_IDCard_Back(self, driver):
        #��������֤����
        self.Cel_NewOrder_4.el_NewOrder4_IDCard_Back(driver).click()
        act_Camera = "com.giveu.corder.ordercreate.activity.CameraActivity"
        driver.wait_activity(act_Camera, 20, 1)
        self.Cel_NewOrder_4.el_NewOrder4_Camera_Shot(driver).click()

    def  b_NewOrder_4_startDate(self, driver, startDate):
        #��ʼ���ڣ�2011/11/11
        hDate = self.Cel_NewOrder_4.el_NewOrder4_ID_DateStart(driver)
        self.C_sel_Rewrite.send_keys(hDate, startDate)

    def b_NewOrder_4_EndDate(self, driver, endDate):
        # �������ڣ�2016/11/11
        hDate = self.Cel_NewOrder_4.el_NewOrder4_ID_DateEnd(driver)
        self.C_sel_Rewrite.send_keys(hDate, endDate)

    def b_NewOrder_4_Phone(self, driver, phone):
        hPhone = self.Cel_NewOrder_4.el_NewOrder4_Phone(driver)
        self.C_sel_Rewrite.send_keys(hPhone, phone)

    def b_NewOrder_4_Submit(self, driver):
        """�ύ"""
        self.Cel_NewOrder_4.el_NewOrder4_Submit(driver)

    #----------------------------------------------------------------------
    #ҵ�����
    # ----------------------------------------------------------------------

    def b_NewOrder_3_Add_GoodInfo(self, driver, subCategory, brand, sku):
        #��д��Ʒ��Ϣ
        self.b_NewOrder_3_Choose_SubCategory(driver, subCategory)
        self.b_NewOrder_3_Check_SubCategory(driver, subCategory)
        self.b_NewOrder_3_Choose_Brand(driver, brand)
        self.b_NewOrder_3_Check_brand(driver, brand)
        self.b_NewOrder_3_Choose_SKU(driver, sku)
        self.b_NewOrder_3_Check_SKU(driver, sku)

    def b_NewOrder_3_Submit(self, driver):
        """�ύ����һ��"""
        self.Cel_NewOrder_3.el_NewOrder3_Next(driver).click()

    def b_NewOrder_4_IDInfo(self, driver, cName, idNo, l_addr, addrDetail, startDate, endDate, phone):
        """��дIDInfo"""
        #����
        self.b_NewOrder_4_Upload_IDFront(driver)
        act_CustomerInfo = "com.giveu.corder.ordercreate.activity.UploadIdCardActivity"
        driver.wait_activity(act_CustomerInfo, 20, 1)
        #����
        self.b_NewOrder_4_cName(driver, cName)
        #����֤����
        self.b_NewOrder_4_IDNo(driver, idNo)
        #ѡ��ʡ����
        self.b_NewOrder_4_parentAddr(driver, l_addr)
        #��ϸ��ַ
        self.b_NewOrder_4_AddressDetail(driver, addrDetail)

        #����
        self.b_NewOrder_4_IDCard_Back(driver)
        self.b_NewOrder_4_startDate(driver, startDate)
        self.b_NewOrder_4_EndDate(driver, endDate)
        self.b_NewOrder_4_Phone(driver, phone)

    def b_NewOrder_5_Upload_GroupPhoto(self, driver):
        #�ϴ���Ա��Ӱ
        self.Cel_NewOrder_5.el_NewOrder5_GroupPhoto_click(driver).click()
        act_Camera = "com.android.camera.Camera"
        driver.wait_activity(act_Camera, 20, 1)
        self.Cel_NewOrder_5.el_NewOrder5_Camera_Shot(driver).click()
        self.Cel_NewOrder_5.el_NewOrder5_Camera_Done(driver).click()

    def b_NewOrder_5_Submit(self, driver):
        #�ύ
        self.Cel_NewOrder_5.el_NewOrder5_Submit(driver).click()