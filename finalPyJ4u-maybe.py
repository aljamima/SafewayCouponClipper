#/usr/bin/python3
##### authenticate only #############
import requests 

username = "shawnmullaney@hotmail.com"
password = "poopoo11"
import requests



def add_coupon_by_id(id, store_id, type):
	headers = {
    'SWY_SSO_TOKEN': '<SWY_SSO_TOKEN> jwt',
    'Content-Type': 'application/json',
	}

	params = (
	    ('storeId', '792'),
	)
	t = Template('{"items":[{"clipType":"C","itemId":"${id}","itemType":"${type}"},{"clipType":"L","itemId":"${id}","itemType":"${type}"}]}')
	data = t.substitute(id=str(id), type=str(type))

	response = requests.post('https://www.safeway.com/abs/pub/web/j4u/api/offers/clip', headers=headers, params=params, data=data)
	print(response.status_code)

add_coupon_by_id(836190395, 0, "PD")