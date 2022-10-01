def com_x_pay_y(pax,par_head,come_x=4,pay_y=3):
   total = (pax // come_x) * (pay_y * par_head) + (pax % come_x)
   return total
print(com_x_pay_y(10,250,7,5))
## edit file 1