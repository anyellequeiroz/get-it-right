.DEFAULT_GOAL := default
#################### PACKAGE ACTIONS ###################

run_api:
	uvicorn app.main:app --reload
