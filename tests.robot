*** Settings ***
Library    RequestsLibrary
Library    Collections
Library         testStarWars.py
Library         testStarWars.StarWarTester

*** Variables ***

*** Test Cases ***
Get All Movies and Check Count
    ${movies}=    Get All Movies
    ${json_response}=    Set Variable    ${movies.json()}
    ${count}=    Set Variable    ${json_response['count']}
    Should Be Equal As Integers    ${count}    6
    Log    The count is ${count}

Get Specific Movie and Check Director
    ${movie}=    Get Specific Movie    3
    ${json_response}=    Set Variable    ${movie.json()}
    ${director}=    Set Variable    ${json_response['director']}
    Should Be Equal    ${director}    Richard Marquand

Get Fifth Movie and Check Producers
    ${movie}=    Get Specific Movie    5
    ${json_response}=    Set Variable    ${movie.json()}
    ${producers}=    Set Variable    ${json_response['producer']}
    Should Not Contain    ${producers}    Gary Kurtz, George Lucas
