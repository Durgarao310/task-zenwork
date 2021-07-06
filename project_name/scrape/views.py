

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def sca(request):
    if request.method == 'GET':
        # Create your views here.
        url = 'https://sanctionssearch.ofac.treas.gov/'
        # driver = webdriver.Chrome('chromedriver.exe')
        driver = webdriver.Chrome(ChromeDriverManager().install())
        
        driver.get(url)
        driver.implicitly_wait(10)

        # driver.find_element_by_id('ctl00_MainContent_ddlCountry').click()
        driver.find_element_by_xpath('//*[@id="ctl00_MainContent_ddlCountry"]/option[163]').click()
        driver.find_element_by_id('ctl00_MainContent_btnSearch').click()

        el1 =  driver.find_element_by_id('gvSearchResults')
        el2 = el1.find_element_by_tag_name('tbody')

        el3 = el2.find_elements_by_tag_name('tr')

        el11 =  driver.find_element_by_id('resultsHeaderTable')
        el21 = el11.find_element_by_tag_name('tbody')

        el31 = el21.find_element_by_tag_name('tr')
        el41 = el31.find_elements_by_tag_name('td')
        
        scrapped_data = []

        name = el41[0].text
        address = el41[1].text
        type = el41[2].text
        program = el41[3].text
        lis = el41[4].text
        score = el41[5].text


        for i in range(len(el3)):
            scrap_data = {}
            el5 = el3[i].find_elements_by_tag_name('td')
            scrap_data['id'] = i
            scrap_data[name]=el5[0].text
            scrap_data[address]=el5[1].text
            scrap_data[type]=el5[2].text
            scrap_data[program]=el5[3].text
            scrap_data[lis]=el5[4].text
            scrap_data[score]=el5[5].text
            scrapped_data.append(scrap_data)

        return Response(scrapped_data)