from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts .globals import ChartType, SymbolType
geo = Geo()
geo.add_schema(maptype='china')
geo.add("",[("北京",302.7528),("上海",325.552),("天津",141.435),("长春",126.6364),("沈阳",442.0632),
            ("呼和浩特",424.1625),("石家庄",387.8718),("乌鲁木齐",326.0904),('哈尔滨',257.0743),("兰州",136.4721),("西宁",37.929),
            ("银川",117.8946),("郑州",411.9926),("济南",985.2719),("太原",708.6261),("重庆",186.2957),
            ("合肥",299.0422),("长沙",269.7866),("武汉",344.0147),("南京",621.9727),("西安",281.02),
            ("成都",317.9774),("贵阳",268.8874),("昆明",235.8295),("南宁",193.8509),
            ("拉萨",0),("杭州",454.9789),("南昌",151.0167),("广州",636.7293),
            ("福州",268.4812),("台北",0),("海口",61.6478),("香港",0),("澳门",0),],type_=ChartType.EFFECT_SCATTER)
geo.add("carbon footprint flow",
[("河北","北京"),("山西","北京"),("内蒙古","北京"),("辽宁","北京"),("吉林","北京"),
 ('黑龙江','北京'),('江苏','北京'),('浙江','北京'),('安徽','北京'),('江西','北京'),
 ('山东', '北京'), ('河南', '北京'), ('湖南', '北京'), ('广东', '北京'), ('广西', '北京'),
 ('重庆', '北京'), ('陕西', '北京'), ('宁夏', '北京'), ('新疆', '北京'), ('河北', '天津'),
 ('河北', '山西'), ('河北', '内蒙古'), ('河北', '辽宁'), ('河北', '黑龙江'), ('河北', '上海'),
 ('河北', '江苏'), ('河北', '浙江'), ('河北', '福建'), ('河北', '山东'), ('河北', '河南'),
 ('河北', '湖北'), ('河北', '广东'), ('河北', '重庆'), ('河北', '四川'), ('河北', '贵州'),
 ('河北', '云南'), ('河北', '陕西'), ('内蒙古', '山西'), ('黑龙江', '山西'), ('江苏', '山西'),
 ('浙江', '山西'), ('安徽', '山西'), ('江西', '山西'), ('山西', '山东'), ('河南', '山西'),
 ('湖南', '山西'), ('内蒙古', '辽宁'), ('内蒙古', '上海'), ('内蒙古', '江苏'), ('内蒙古', '浙江'),
 ('内蒙古', '山东'), ('内蒙古', '河南'), ('内蒙古', '广东'), ('内蒙古', '重庆'), ('内蒙古', '贵州'),
 ('内蒙古', '云南'), ('内蒙古', '陕西'), ('内蒙古', '新疆'), ('吉林', '辽宁'), ('辽宁', '上海'),
 ('辽宁', '浙江'), ('辽宁', '山东'), ('辽宁', '广东'), ('吉林', '上海'), ('吉林', '浙江'),
 ('吉林', '山东'), ('吉林', '广东'), ('江苏', '上海'), ('安徽', '上海'), ('河南', '上海'),
 ('陕西', '上海'), ('宁夏', '上海'), ('新疆', '上海'), ('江苏', '浙江'), ('江苏', '山东'),
 ('江苏', '广东'), ('江苏', '贵州'), ('江苏', '陕西'), ('宁夏', '江苏'), ('新疆', '江苏'),
 ('安徽', '浙江'), ('江西', '浙江'), ('浙江', '山东'), ('河南', '浙江'), ('宁夏', '浙江'),
 ('新疆', '浙江'), ('安徽', '山东'), ('安徽', '广东'), ('江西', '山东'), ('江西', '广东'),
 ('河南', '山东'), ('湖南', '山东'), ('新疆', '山东'), ('河南', '广东'), ('河南', '四川'),
 ('广西', '广东'), ('宁夏', '广东'), ('新疆', '广东'), ('新疆', '云南'), ('新疆', '陕西'),
 ],
type_=ChartType.LINES,
effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW,symbol_size=5,color="yellow"),
linestyle_opts=opts.LineStyleOpts(curve=0.2),
is_large=True)
geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=1000,min_=60),title_opts=opts.TitleOpts(title="carbon footprint"))
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
geo.render("D:/训练/mychart.html")

















