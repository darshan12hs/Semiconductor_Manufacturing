from flask import Flask, render_template,request
import joblib

# Load the model
model=joblib.load('xgb_model_file.pkl')

# Initialize the app
app=Flask(__name__)
# print(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/process',methods=['post'])
def form_data():
    Feature_0=request.form.get("Feature_0")
    Feature_1=request.form.get("Feature_1")
    Feature_2=request.form.get("Feature_2")
    Feature_3=request.form.get("Feature_3")
    Feature_4=request.form.get("Feature_4")
    Feature_5=request.form.get("Feature_5")
    Feature_6=request.form.get("Feature_6")
    Feature_7=request.form.get("Feature_7")
    Feature_8=request.form.get("Feature_8")
    Feature_9=request.form.get("Feature_9")
    Feature_10=request.form.get("Feature_10")
    Feature_11=request.form.get("Feature_11")
    Feature_12=request.form.get("Feature_12")
    Feature_13=request.form.get("Feature_13")
    Feature_14=request.form.get("Feature_14")
    Feature_15=request.form.get("Feature_15")
    Feature_16=request.form.get("Feature_16")
    Feature_17=request.form.get("Feature_17")
    Feature_18=request.form.get("Feature_18")
    Feature_19=request.form.get("Feature_19")
    Feature_20=request.form.get("Feature_20")
    Feature_21=request.form.get("Feature_21")
    Feature_22=request.form.get("Feature_22")
    Feature_23=request.form.get("Feature_23")
    Feature_24=request.form.get("Feature_24")
    Feature_25=request.form.get("Feature_25")
    Feature_26=request.form.get("Feature_26")
    Feature_27=request.form.get("Feature_27")
    Feature_28=request.form.get("Feature_28")
    Feature_29=request.form.get("Feature_29")
    Feature_30=request.form.get("Feature_30")
    Feature_31=request.form.get("Feature_31")
    Feature_32=request.form.get("Feature_32")
    Feature_33=request.form.get("Feature_33")
    Feature_34=request.form.get("Feature_34")
    Feature_35=request.form.get("Feature_35")
    Feature_36=request.form.get("Feature_36")
    Feature_37=request.form.get("Feature_37")
    Feature_38=request.form.get("Feature_38")
    Feature_39=request.form.get("Feature_39")
    Feature_40=request.form.get("Feature_40")
    Feature_41=request.form.get("Feature_41")
    Feature_42=request.form.get("Feature_42")
    Feature_43=request.form.get("Feature_43")
    Feature_44=request.form.get("Feature_44")
    Feature_45=request.form.get("Feature_45")
    Feature_46=request.form.get("Feature_46")
    Feature_47=request.form.get("Feature_47")
    Feature_48=request.form.get("Feature_48")
    Feature_49=request.form.get("Feature_49")
    Feature_50=request.form.get("Feature_50")
    Feature_51=request.form.get("Feature_51")
    Feature_52=request.form.get("Feature_52")
    Feature_53=request.form.get("Feature_53")
    Feature_54=request.form.get("Feature_54")
    Feature_55=request.form.get("Feature_55")
    Feature_56=request.form.get("Feature_56")
    Feature_57=request.form.get("Feature_57")
    Feature_58=request.form.get("Feature_58")
    Feature_59=request.form.get("Feature_59")
    Feature_60=request.form.get("Feature_60")
    Feature_61=request.form.get("Feature_61")
    Feature_62=request.form.get("Feature_62")
    Feature_63=request.form.get("Feature_63")
    Feature_64=request.form.get("Feature_64")
    Feature_65=request.form.get("Feature_65")
    Feature_66=request.form.get("Feature_66")
    Feature_67=request.form.get("Feature_67")
    Feature_68=request.form.get("Feature_68")
    Feature_69=request.form.get("Feature_69")
    Feature_70=request.form.get("Feature_70")
    Feature_71=request.form.get("Feature_71")
    Feature_74=request.form.get("Feature_74")
    Feature_75=request.form.get("Feature_75")
    Feature_76=request.form.get("Feature_76")
    Feature_77=request.form.get("Feature_77")
    Feature_78=request.form.get("Feature_78")
    Feature_79=request.form.get("Feature_79")
    Feature_80=request.form.get("Feature_80")
    Feature_81=request.form.get("Feature_81")
    Feature_82=request.form.get("Feature_82")
    Feature_83=request.form.get("Feature_83")
    Feature_84=request.form.get("Feature_84")
    Feature_86=request.form.get("Feature_86")
    Feature_87=request.form.get("Feature_87")
    Feature_88=request.form.get("Feature_88")
    Feature_89=request.form.get("Feature_89")
    Feature_90=request.form.get("Feature_90")
    Feature_91=request.form.get("Feature_91")
    Feature_92=request.form.get("Feature_92")
    Feature_93=request.form.get("Feature_93")
    Feature_94=request.form.get("Feature_94")
    Feature_95=request.form.get("Feature_95")
    Feature_96=request.form.get("Feature_96")
    Feature_97=request.form.get("Feature_97")
    Feature_98=request.form.get("Feature_98")
    Feature_99=request.form.get("Feature_99")
    Feature_100=request.form.get("Feature_100")
    Feature_101=request.form.get("Feature_101")
    Feature_102=request.form.get("Feature_102")
    Feature_103=request.form.get("Feature_103")
    Feature_104=request.form.get("Feature_104")
    Feature_105=request.form.get("Feature_105")
    Feature_106=request.form.get("Feature_106")
    Feature_107=request.form.get("Feature_107")
    Feature_108=request.form.get("Feature_108")
    Feature_113=request.form.get("Feature_113")
    Feature_114=request.form.get("Feature_114")
    Feature_115=request.form.get("Feature_115")
    Feature_116=request.form.get("Feature_116")
    Feature_117=request.form.get("Feature_117")
    Feature_118=request.form.get("Feature_118")
    Feature_119=request.form.get("Feature_119")
    Feature_120=request.form.get("Feature_120")
    Feature_121=request.form.get("Feature_121")
    Feature_122=request.form.get("Feature_122")
    Feature_123=request.form.get("Feature_123")
    Feature_124=request.form.get("Feature_124")
    Feature_125=request.form.get("Feature_125")
    Feature_126=request.form.get("Feature_126")
    Feature_127=request.form.get("Feature_127")
    Feature_128=request.form.get("Feature_128")
    Feature_129=request.form.get("Feature_129")
    Feature_130=request.form.get("Feature_130")
    Feature_131=request.form.get("Feature_131")
    Feature_132=request.form.get("Feature_132")
    Feature_133=request.form.get("Feature_133")
    Feature_134=request.form.get("Feature_134")
    Feature_135=request.form.get("Feature_135")
    Feature_136=request.form.get("Feature_136")
    Feature_137=request.form.get("Feature_137")
    Feature_138=request.form.get("Feature_138")
    Feature_139=request.form.get("Feature_139")
    Feature_140=request.form.get("Feature_140")
    Feature_141=request.form.get("Feature_141")
    Feature_142=request.form.get("Feature_142")
    Feature_143=request.form.get("Feature_143")
    Feature_144=request.form.get("Feature_144")
    Feature_145=request.form.get("Feature_145")
    Feature_146=request.form.get("Feature_146")
    Feature_147=request.form.get("Feature_147")
    Feature_148=request.form.get("Feature_148")
    Feature_149=request.form.get("Feature_149")
    Feature_150=request.form.get("Feature_150")
    Feature_151=request.form.get("Feature_151")
    Feature_152=request.form.get("Feature_152")
    Feature_153=request.form.get("Feature_153")
    Feature_154=request.form.get("Feature_154")
    Feature_155=request.form.get("Feature_155")
    Feature_156=request.form.get("Feature_156")
    Feature_159=request.form.get("Feature_159")
    Feature_160=request.form.get("Feature_160")
    Feature_161=request.form.get("Feature_161")
    Feature_162=request.form.get("Feature_162")
    Feature_163=request.form.get("Feature_163")
    Feature_164=request.form.get("Feature_164")
    Feature_165=request.form.get("Feature_165")
    Feature_166=request.form.get("Feature_166")
    Feature_167=request.form.get("Feature_167")
    Feature_168=request.form.get("Feature_168")
    Feature_169=request.form.get("Feature_169")
    Feature_170=request.form.get("Feature_170")
    Feature_171=request.form.get("Feature_171")
    Feature_172=request.form.get("Feature_172")
    Feature_173=request.form.get("Feature_173")
    Feature_174=request.form.get("Feature_174")
    Feature_175=request.form.get("Feature_175")
    Feature_176=request.form.get("Feature_176")
    Feature_177=request.form.get("Feature_177")
    Feature_178=request.form.get("Feature_178")
    Feature_179=request.form.get("Feature_179")
    Feature_180=request.form.get("Feature_180")
    Feature_181=request.form.get("Feature_181")
    Feature_182=request.form.get("Feature_182")
    Feature_183=request.form.get("Feature_183")
    Feature_184=request.form.get("Feature_184")
    Feature_185=request.form.get("Feature_185")
    Feature_186=request.form.get("Feature_186")
    Feature_187=request.form.get("Feature_187")
    Feature_188=request.form.get("Feature_188")
    Feature_189=request.form.get("Feature_189")
    Feature_190=request.form.get("Feature_190")
    Feature_191=request.form.get("Feature_191")
    Feature_192=request.form.get("Feature_192")
    Feature_193=request.form.get("Feature_193")
    Feature_194=request.form.get("Feature_194")
    Feature_195=request.form.get("Feature_195")
    Feature_196=request.form.get("Feature_196")
    Feature_197=request.form.get("Feature_197")
    Feature_198=request.form.get("Feature_198")
    Feature_199=request.form.get("Feature_199")
    Feature_200=request.form.get("Feature_200")
    Feature_201=request.form.get("Feature_201")
    Feature_202=request.form.get("Feature_202")
    Feature_203=request.form.get("Feature_203")
    Feature_204=request.form.get("Feature_204")
    Feature_205=request.form.get("Feature_205")
    Feature_206=request.form.get("Feature_206")
    Feature_207=request.form.get("Feature_207")
    Feature_208=request.form.get("Feature_208")
    Feature_209=request.form.get("Feature_209")
    Feature_210=request.form.get("Feature_210")
    Feature_211=request.form.get("Feature_211")
    Feature_212=request.form.get("Feature_212")
    Feature_213=request.form.get("Feature_213")
    Feature_214=request.form.get("Feature_214")
    Feature_215=request.form.get("Feature_215")
    Feature_216=request.form.get("Feature_216")
    Feature_217=request.form.get("Feature_217")
    Feature_218=request.form.get("Feature_218")
    Feature_219=request.form.get("Feature_219")
    Feature_221=request.form.get("Feature_221")
    Feature_222=request.form.get("Feature_222")
    Feature_223=request.form.get("Feature_223")
    Feature_224=request.form.get("Feature_224")
    Feature_225=request.form.get("Feature_225")
    Feature_226=request.form.get("Feature_226")
    Feature_227=request.form.get("Feature_227")
    Feature_228=request.form.get("Feature_228")
    Feature_229=request.form.get("Feature_229")
    Feature_230=request.form.get("Feature_230")
    Feature_231=request.form.get("Feature_231")
    Feature_232=request.form.get("Feature_232")
    Feature_233=request.form.get("Feature_233")
    Feature_234=request.form.get("Feature_234")
    Feature_235=request.form.get("Feature_235")
    Feature_236=request.form.get("Feature_236")
    Feature_237=request.form.get("Feature_237")
    Feature_238=request.form.get("Feature_238")
    Feature_239=request.form.get("Feature_239")
    Feature_240=request.form.get("Feature_240")
    Feature_241=request.form.get("Feature_241")
    Feature_242=request.form.get("Feature_242")
    Feature_243=request.form.get("Feature_243")
    Feature_248=request.form.get("Feature_248")
    Feature_249=request.form.get("Feature_249")
    Feature_250=request.form.get("Feature_250")
    Feature_251=request.form.get("Feature_251")
    Feature_252=request.form.get("Feature_252")
    Feature_253=request.form.get("Feature_253")
    Feature_254=request.form.get("Feature_254")
    Feature_255=request.form.get("Feature_255")
    Feature_256=request.form.get("Feature_256")
    Feature_257=request.form.get("Feature_257")
    Feature_258=request.form.get("Feature_258")
    Feature_259=request.form.get("Feature_259")
    Feature_260=request.form.get("Feature_260")
    Feature_261=request.form.get("Feature_261")
    Feature_262=request.form.get("Feature_262")
    Feature_263=request.form.get("Feature_263")
    Feature_264=request.form.get("Feature_264")
    Feature_265=request.form.get("Feature_265")
    Feature_266=request.form.get("Feature_266")
    Feature_267=request.form.get("Feature_267")
    Feature_268=request.form.get("Feature_268")
    Feature_269=request.form.get("Feature_269")
    Feature_270=request.form.get("Feature_270")
    Feature_271=request.form.get("Feature_271")
    Feature_272=request.form.get("Feature_272")
    Feature_273=request.form.get("Feature_273")
    Feature_274=request.form.get("Feature_274")
    Feature_275=request.form.get("Feature_275")
    Feature_276=request.form.get("Feature_276")
    Feature_277=request.form.get("Feature_277")
    Feature_278=request.form.get("Feature_278")
    Feature_279=request.form.get("Feature_279")
    Feature_280=request.form.get("Feature_280")
    Feature_281=request.form.get("Feature_281")
    Feature_282=request.form.get("Feature_282")
    Feature_283=request.form.get("Feature_283")
    Feature_284=request.form.get("Feature_284")
    Feature_285=request.form.get("Feature_285")
    Feature_286=request.form.get("Feature_286")
    Feature_287=request.form.get("Feature_287")
    Feature_288=request.form.get("Feature_288")
    Feature_289=request.form.get("Feature_289")
    Feature_290=request.form.get("Feature_290")
    Feature_291=request.form.get("Feature_291")
    Feature_294=request.form.get("Feature_294")
    Feature_295=request.form.get("Feature_295")
    Feature_296=request.form.get("Feature_296")
    Feature_297=request.form.get("Feature_297")
    Feature_298=request.form.get("Feature_298")
    Feature_299=request.form.get("Feature_299")
    Feature_300=request.form.get("Feature_300")
    Feature_301=request.form.get("Feature_301")
    Feature_302=request.form.get("Feature_302")
    Feature_303=request.form.get("Feature_303")
    Feature_304=request.form.get("Feature_304")
    Feature_305=request.form.get("Feature_305")
    Feature_306=request.form.get("Feature_306")
    Feature_307=request.form.get("Feature_307")
    Feature_308=request.form.get("Feature_308")
    Feature_309=request.form.get("Feature_309")
    Feature_310=request.form.get("Feature_310")
    Feature_311=request.form.get("Feature_311")
    Feature_312=request.form.get("Feature_312")
    Feature_313=request.form.get("Feature_313")
    Feature_314=request.form.get("Feature_314")
    Feature_315=request.form.get("Feature_315")
    Feature_316=request.form.get("Feature_316")
    Feature_317=request.form.get("Feature_317")
    Feature_318=request.form.get("Feature_318")
    Feature_319=request.form.get("Feature_319")
    Feature_320=request.form.get("Feature_320")
    Feature_321=request.form.get("Feature_321")
    Feature_322=request.form.get("Feature_322")
    Feature_323=request.form.get("Feature_323")
    Feature_324=request.form.get("Feature_324")
    Feature_325=request.form.get("Feature_325")
    Feature_326=request.form.get("Feature_326")
    Feature_327=request.form.get("Feature_327")
    Feature_328=request.form.get("Feature_328")
    Feature_329=request.form.get("Feature_329")
    Feature_330=request.form.get("Feature_330")
    Feature_331=request.form.get("Feature_331")
    Feature_332=request.form.get("Feature_332")
    Feature_333=request.form.get("Feature_333")
    Feature_334=request.form.get("Feature_334")
    Feature_335=request.form.get("Feature_335")
    Feature_336=request.form.get("Feature_336")
    Feature_337=request.form.get("Feature_337")
    Feature_338=request.form.get("Feature_338")
    Feature_339=request.form.get("Feature_339")
    Feature_340=request.form.get("Feature_340")
    Feature_341=request.form.get("Feature_341")
    Feature_342=request.form.get("Feature_342")
    Feature_343=request.form.get("Feature_343")
    Feature_344=request.form.get("Feature_344")
    Feature_347=request.form.get("Feature_347")
    Feature_348=request.form.get("Feature_348")
    Feature_349=request.form.get("Feature_349")
    Feature_350=request.form.get("Feature_350")
    Feature_351=request.form.get("Feature_351")
    Feature_352=request.form.get("Feature_352")
    Feature_353=request.form.get("Feature_353")
    Feature_354=request.form.get("Feature_354")
    Feature_355=request.form.get("Feature_355")
    Feature_356=request.form.get("Feature_356")
    Feature_357=request.form.get("Feature_357")
    Feature_359=request.form.get("Feature_359")
    Feature_360=request.form.get("Feature_360")
    Feature_361=request.form.get("Feature_361")
    Feature_362=request.form.get("Feature_362")
    Feature_363=request.form.get("Feature_363")
    Feature_364=request.form.get("Feature_364")
    Feature_365=request.form.get("Feature_365")
    Feature_366=request.form.get("Feature_366")
    Feature_367=request.form.get("Feature_367")
    Feature_368=request.form.get("Feature_368")
    Feature_369=request.form.get("Feature_369")
    Feature_370=request.form.get("Feature_370")
    Feature_371=request.form.get("Feature_371")
    Feature_372=request.form.get("Feature_372")
    Feature_373=request.form.get("Feature_373")
    Feature_374=request.form.get("Feature_374")
    Feature_375=request.form.get("Feature_375")
    Feature_376=request.form.get("Feature_376")
    Feature_377=request.form.get("Feature_377")
    Feature_378=request.form.get("Feature_378")
    Feature_379=request.form.get("Feature_379")
    Feature_380=request.form.get("Feature_380")
    Feature_381=request.form.get("Feature_381")
    Feature_386=request.form.get("Feature_386")
    Feature_387=request.form.get("Feature_387")
    Feature_388=request.form.get("Feature_388")
    Feature_389=request.form.get("Feature_389")
    Feature_390=request.form.get("Feature_390")
    Feature_391=request.form.get("Feature_391")
    Feature_392=request.form.get("Feature_392")
    Feature_393=request.form.get("Feature_393")
    Feature_394=request.form.get("Feature_394")
    Feature_395=request.form.get("Feature_395")
    Feature_396=request.form.get("Feature_396")
    Feature_397=request.form.get("Feature_397")
    Feature_398=request.form.get("Feature_398")
    Feature_399=request.form.get("Feature_399")
    Feature_400=request.form.get("Feature_400")
    Feature_401=request.form.get("Feature_401")
    Feature_402=request.form.get("Feature_402")
    Feature_403=request.form.get("Feature_403")
    Feature_404=request.form.get("Feature_404")
    Feature_405=request.form.get("Feature_405")
    Feature_406=request.form.get("Feature_406")
    Feature_407=request.form.get("Feature_407")
    Feature_408=request.form.get("Feature_408")
    Feature_409=request.form.get("Feature_409")
    Feature_410=request.form.get("Feature_410")
    Feature_411=request.form.get("Feature_411")
    Feature_412=request.form.get("Feature_412")
    Feature_413=request.form.get("Feature_413")
    Feature_414=request.form.get("Feature_414")
    Feature_415=request.form.get("Feature_415")
    Feature_416=request.form.get("Feature_416")
    Feature_417=request.form.get("Feature_417")
    Feature_418=request.form.get("Feature_418")
    Feature_419=request.form.get("Feature_419")
    Feature_420=request.form.get("Feature_420")
    Feature_421=request.form.get("Feature_421")
    Feature_422=request.form.get("Feature_422")
    Feature_423=request.form.get("Feature_423")
    Feature_424=request.form.get("Feature_424")
    Feature_425=request.form.get("Feature_425")
    Feature_426=request.form.get("Feature_426")
    Feature_427=request.form.get("Feature_427")
    Feature_428=request.form.get("Feature_428")
    Feature_429=request.form.get("Feature_429")
    Feature_430=request.form.get("Feature_430")
    Feature_431=request.form.get("Feature_431")
    Feature_432=request.form.get("Feature_432")
    Feature_433=request.form.get("Feature_433")
    Feature_434=request.form.get("Feature_434")
    Feature_435=request.form.get("Feature_435")
    Feature_436=request.form.get("Feature_436")
    Feature_437=request.form.get("Feature_437")
    Feature_438=request.form.get("Feature_438")
    Feature_439=request.form.get("Feature_439")
    Feature_440=request.form.get("Feature_440")
    Feature_441=request.form.get("Feature_441")
    Feature_442=request.form.get("Feature_442")
    Feature_443=request.form.get("Feature_443")
    Feature_444=request.form.get("Feature_444")
    Feature_445=request.form.get("Feature_445")
    Feature_446=request.form.get("Feature_446")
    Feature_447=request.form.get("Feature_447")
    Feature_448=request.form.get("Feature_448")
    Feature_449=request.form.get("Feature_449")
    Feature_450=request.form.get("Feature_450")
    Feature_451=request.form.get("Feature_451")
    Feature_452=request.form.get("Feature_452")
    Feature_453=request.form.get("Feature_453")
    Feature_454=request.form.get("Feature_454")
    Feature_455=request.form.get("Feature_455")
    Feature_456=request.form.get("Feature_456")
    Feature_457=request.form.get("Feature_457")
    Feature_458=request.form.get("Feature_458")
    Feature_459=request.form.get("Feature_459")
    Feature_460=request.form.get("Feature_460")
    Feature_461=request.form.get("Feature_461")
    Feature_462=request.form.get("Feature_462")
    Feature_463=request.form.get("Feature_463")
    Feature_464=request.form.get("Feature_464")
    Feature_465=request.form.get("Feature_465")
    Feature_466=request.form.get("Feature_466")
    Feature_467=request.form.get("Feature_467")
    Feature_468=request.form.get("Feature_468")
    Feature_469=request.form.get("Feature_469")
    Feature_470=request.form.get("Feature_470")
    Feature_471=request.form.get("Feature_471")
    Feature_472=request.form.get("Feature_472")
    Feature_473=request.form.get("Feature_473")
    Feature_474=request.form.get("Feature_474")
    Feature_475=request.form.get("Feature_475")
    Feature_476=request.form.get("Feature_476")
    Feature_477=request.form.get("Feature_477")
    Feature_478=request.form.get("Feature_478")
    Feature_479=request.form.get("Feature_479")
    Feature_480=request.form.get("Feature_480")
    Feature_481=request.form.get("Feature_481")
    Feature_482=request.form.get("Feature_482")
    Feature_483=request.form.get("Feature_483")
    Feature_484=request.form.get("Feature_484")
    Feature_485=request.form.get("Feature_485")
    Feature_486=request.form.get("Feature_486")
    Feature_487=request.form.get("Feature_487")
    Feature_488=request.form.get("Feature_488")
    Feature_489=request.form.get("Feature_489")
    Feature_490=request.form.get("Feature_490")
    Feature_491=request.form.get("Feature_491")
    Feature_493=request.form.get("Feature_493")
    Feature_494=request.form.get("Feature_494")
    Feature_495=request.form.get("Feature_495")
    Feature_496=request.form.get("Feature_496")
    Feature_497=request.form.get("Feature_497")
    Feature_498=request.form.get("Feature_498")
    Feature_499=request.form.get("Feature_499")
    Feature_500=request.form.get("Feature_500")
    Feature_501=request.form.get("Feature_501")
    Feature_502=request.form.get("Feature_502")
    Feature_503=request.form.get("Feature_503")
    Feature_504=request.form.get("Feature_504")
    Feature_505=request.form.get("Feature_505")
    Feature_506=request.form.get("Feature_506")
    Feature_507=request.form.get("Feature_507")
    Feature_508=request.form.get("Feature_508")
    Feature_509=request.form.get("Feature_509")
    Feature_510=request.form.get("Feature_510")
    Feature_511=request.form.get("Feature_511")
    Feature_512=request.form.get("Feature_512")
    Feature_513=request.form.get("Feature_513")
    Feature_514=request.form.get("Feature_514")
    Feature_515=request.form.get("Feature_515")
    Feature_520=request.form.get("Feature_520")
    Feature_521=request.form.get("Feature_521")
    Feature_522=request.form.get("Feature_522")
    Feature_523=request.form.get("Feature_523")
    Feature_524=request.form.get("Feature_524")
    Feature_525=request.form.get("Feature_525")
    Feature_526=request.form.get("Feature_526")
    Feature_527=request.form.get("Feature_527")
    Feature_528=request.form.get("Feature_528")
    Feature_529=request.form.get("Feature_529")
    Feature_530=request.form.get("Feature_530")
    Feature_531=request.form.get("Feature_531")
    Feature_532=request.form.get("Feature_532")
    Feature_533=request.form.get("Feature_533")
    Feature_534=request.form.get("Feature_534")
    Feature_535=request.form.get("Feature_535")
    Feature_536=request.form.get("Feature_536")
    Feature_537=request.form.get("Feature_537")
    Feature_538=request.form.get("Feature_538")
    Feature_539=request.form.get("Feature_539")
    Feature_540=request.form.get("Feature_540")
    Feature_541=request.form.get("Feature_541")
    Feature_542=request.form.get("Feature_542")
    Feature_543=request.form.get("Feature_543")
    Feature_544=request.form.get("Feature_544")
    Feature_545=request.form.get("Feature_545")
    Feature_546=request.form.get("Feature_546")
    Feature_547=request.form.get("Feature_547")
    Feature_548=request.form.get("Feature_548")
    Feature_549=request.form.get("Feature_549")
    Feature_550=request.form.get("Feature_550")
    Feature_551=request.form.get("Feature_551")
    Feature_552=request.form.get("Feature_552")
    Feature_553=request.form.get("Feature_553")
    Feature_554=request.form.get("Feature_554")
    Feature_555=request.form.get("Feature_555")
    Feature_556=request.form.get("Feature_556")
    Feature_557=request.form.get("Feature_557")
    Feature_558=request.form.get("Feature_558")
    Feature_559=request.form.get("Feature_559")
    Feature_560=request.form.get("Feature_560")
    Feature_561=request.form.get("Feature_561")
    Feature_562=request.form.get("Feature_562")
    Feature_563=request.form.get("Feature_563")
    Feature_564=request.form.get("Feature_564")
    Feature_565=request.form.get("Feature_565")
    Feature_566=request.form.get("Feature_566")
    Feature_567=request.form.get("Feature_567")
    Feature_568=request.form.get("Feature_568")
    Feature_569=request.form.get("Feature_569")
    Feature_570=request.form.get("Feature_570")
    Feature_571=request.form.get("Feature_571")
    Feature_572=request.form.get("Feature_572")
    Feature_573=request.form.get("Feature_573")
    Feature_574=request.form.get("Feature_574")
    Feature_575=request.form.get("Feature_575")
    Feature_576=request.form.get("Feature_576")
    Feature_577=request.form.get("Feature_577")
    Feature_582=request.form.get("Feature_582")
    Feature_583=request.form.get("Feature_583")
    Feature_584=request.form.get("Feature_584")
    Feature_585=request.form.get("Feature_585")
    Feature_586=request.form.get("Feature_586")
    Feature_587=request.form.get("Feature_587")
    Feature_588=request.form.get("Feature_588")
    Feature_589=request.form.get("Feature_589")
    Month=request.form.get("Month")
    Date=request.form.get("Date")
    Week_Day=request.form.get("Week_Day")
    Hour=request.form.get("Hour")
    Minute=request.form.get("Minute")

    result=model.predict([[float(Feature_0), float(Feature_1), float(Feature_2), float(Feature_3), 
                           float(Feature_4), float(Feature_5), float(Feature_6), float(Feature_7), 
                           float(Feature_8), float(Feature_9), float(Feature_10), float(Feature_11), 
                           float(Feature_12), float(Feature_13), float(Feature_14), float(Feature_15), 
                           float(Feature_16), float(Feature_17), float(Feature_18), float(Feature_19), 
                           float(Feature_20), float(Feature_21), float(Feature_22), float(Feature_23), 
                           float(Feature_24), float(Feature_25), float(Feature_26), float(Feature_27), 
                           float(Feature_28), float(Feature_29), float(Feature_30), float(Feature_31), 
                           float(Feature_32), float(Feature_33), float(Feature_34), float(Feature_35), 
                           float(Feature_36), float(Feature_37), float(Feature_38), float(Feature_39), 
                           float(Feature_40), float(Feature_41), float(Feature_42), float(Feature_43), 
                           float(Feature_44), float(Feature_45), float(Feature_46), float(Feature_47), 
                           float(Feature_48), float(Feature_49), float(Feature_50), float(Feature_51), 
                           float(Feature_52), float(Feature_53), float(Feature_54), float(Feature_55), 
                           float(Feature_56), float(Feature_57), float(Feature_58), float(Feature_59), 
                           float(Feature_60), float(Feature_61), float(Feature_62), float(Feature_63), 
                           float(Feature_64), float(Feature_65), float(Feature_66), float(Feature_67), 
                           float(Feature_68), float(Feature_69), float(Feature_70), float(Feature_71), 
                           float(Feature_74), float(Feature_75), 
                           float(Feature_76), float(Feature_77), float(Feature_78), float(Feature_79), 
                           float(Feature_80), float(Feature_81), float(Feature_82), float(Feature_83), 
                           float(Feature_84), float(Feature_86), float(Feature_87), 
                           float(Feature_88), float(Feature_89), float(Feature_90), float(Feature_91), 
                           float(Feature_92), float(Feature_93), float(Feature_94), float(Feature_95), 
                           float(Feature_96), float(Feature_97), float(Feature_98), float(Feature_99), 
                           float(Feature_100), float(Feature_101), float(Feature_102), float(Feature_103), 
                           float(Feature_104), float(Feature_105), float(Feature_106), float(Feature_107), 
                           float(Feature_108), float(Feature_113), float(Feature_114), float(Feature_115), 
                           float(Feature_116), float(Feature_117), float(Feature_118), float(Feature_119), 
                           float(Feature_120), float(Feature_121), float(Feature_122), float(Feature_123), 
                           float(Feature_124), float(Feature_125), float(Feature_126), float(Feature_127), 
                           float(Feature_128), float(Feature_129), float(Feature_130), float(Feature_131), 
                           float(Feature_132), float(Feature_133), float(Feature_134), float(Feature_135), 
                           float(Feature_136), float(Feature_137), float(Feature_138), float(Feature_139), 
                           float(Feature_140), float(Feature_141), float(Feature_142), float(Feature_143), 
                           float(Feature_144), float(Feature_145), float(Feature_146), float(Feature_147), 
                           float(Feature_148), float(Feature_149), float(Feature_150), float(Feature_151), 
                           float(Feature_152), float(Feature_153), float(Feature_154), float(Feature_155), 
                           float(Feature_156), float(Feature_159), 
                           float(Feature_160), float(Feature_161), float(Feature_162), float(Feature_163), 
                           float(Feature_164), float(Feature_165), float(Feature_166), float(Feature_167), 
                           float(Feature_168), float(Feature_169), float(Feature_170), float(Feature_171), 
                           float(Feature_172), float(Feature_173), float(Feature_174), float(Feature_175), 
                           float(Feature_176), float(Feature_177), float(Feature_178), float(Feature_179), 
                           float(Feature_180), float(Feature_181), float(Feature_182), float(Feature_183), 
                           float(Feature_184), float(Feature_185), float(Feature_186), float(Feature_187), 
                           float(Feature_188), float(Feature_189), float(Feature_190), float(Feature_191), 
                           float(Feature_192), float(Feature_193), float(Feature_194), float(Feature_195), 
                           float(Feature_196), float(Feature_197), float(Feature_198), float(Feature_199), 
                           float(Feature_200), float(Feature_201), float(Feature_202), float(Feature_203), 
                           float(Feature_204), float(Feature_205), float(Feature_206), float(Feature_207), 
                           float(Feature_208), float(Feature_209), float(Feature_210), float(Feature_211), 
                           float(Feature_212), float(Feature_213), float(Feature_214), float(Feature_215), 
                           float(Feature_216), float(Feature_217), float(Feature_218), float(Feature_219), 
                           float(Feature_221), float(Feature_222), float(Feature_223), 
                           float(Feature_224), float(Feature_225), float(Feature_226), float(Feature_227), 
                           float(Feature_228), float(Feature_229), float(Feature_230), float(Feature_231), 
                           float(Feature_232), float(Feature_233), float(Feature_234), float(Feature_235), 
                           float(Feature_236), float(Feature_237), float(Feature_238), float(Feature_239), 
                           float(Feature_240), float(Feature_241), float(Feature_242), float(Feature_243), 
                           float(Feature_248), float(Feature_249), float(Feature_250), float(Feature_251), 
                           float(Feature_252), float(Feature_253), float(Feature_254), float(Feature_255), 
                           float(Feature_256), float(Feature_257), float(Feature_258), float(Feature_259), 
                           float(Feature_260), float(Feature_261), float(Feature_262), float(Feature_263), 
                           float(Feature_264), float(Feature_265), float(Feature_266), float(Feature_267), 
                           float(Feature_268), float(Feature_269), float(Feature_270), float(Feature_271), 
                           float(Feature_272), float(Feature_273), float(Feature_274), float(Feature_275), 
                           float(Feature_276), float(Feature_277), float(Feature_278), float(Feature_279), 
                           float(Feature_280), float(Feature_281), float(Feature_282), float(Feature_283), 
                           float(Feature_284), float(Feature_285), float(Feature_286), float(Feature_287), 
                           float(Feature_288), float(Feature_289), float(Feature_290), float(Feature_291), 
                           float(Feature_294), float(Feature_295), 
                           float(Feature_296), float(Feature_297), float(Feature_298), float(Feature_299), 
                           float(Feature_300), float(Feature_301), float(Feature_302), float(Feature_303), 
                           float(Feature_304), float(Feature_305), float(Feature_306), float(Feature_307), 
                           float(Feature_308), float(Feature_309), float(Feature_310), float(Feature_311), 
                           float(Feature_312), float(Feature_313), float(Feature_314), float(Feature_315), 
                           float(Feature_316), float(Feature_317), float(Feature_318), float(Feature_319), 
                           float(Feature_320), float(Feature_321), float(Feature_322), float(Feature_323), 
                           float(Feature_324), float(Feature_325), float(Feature_326), float(Feature_327), 
                           float(Feature_328), float(Feature_329), float(Feature_330), float(Feature_331), 
                           float(Feature_332), float(Feature_333), float(Feature_334), float(Feature_335), 
                           float(Feature_336), float(Feature_337), float(Feature_338), float(Feature_339), 
                           float(Feature_340), float(Feature_341), float(Feature_342), float(Feature_343), 
                           float(Feature_344), float(Feature_347), 
                           float(Feature_348), float(Feature_349), float(Feature_350), float(Feature_351), 
                           float(Feature_352), float(Feature_353), float(Feature_354), float(Feature_355), 
                           float(Feature_356), float(Feature_357), float(Feature_359), 
                           float(Feature_360), float(Feature_361), float(Feature_362), float(Feature_363), 
                           float(Feature_364), float(Feature_365), float(Feature_366), float(Feature_367), 
                           float(Feature_368), float(Feature_369), float(Feature_370), float(Feature_371), 
                           float(Feature_372), float(Feature_373), float(Feature_374), float(Feature_375), 
                           float(Feature_376), float(Feature_377), float(Feature_378), float(Feature_379), 
                           float(Feature_380), float(Feature_381), float(Feature_386), float(Feature_387), 
                           float(Feature_388), float(Feature_389), float(Feature_390), float(Feature_391), 
                           float(Feature_392), float(Feature_393), float(Feature_394), float(Feature_395), 
                           float(Feature_396), float(Feature_397), float(Feature_398), float(Feature_399), 
                           float(Feature_400), float(Feature_401), float(Feature_402), float(Feature_403), 
                           float(Feature_404), float(Feature_405), float(Feature_406), float(Feature_407), 
                           float(Feature_408), float(Feature_409), float(Feature_410), float(Feature_411), 
                           float(Feature_412), float(Feature_413), float(Feature_414), float(Feature_415), 
                           float(Feature_416), float(Feature_417), float(Feature_418), float(Feature_419), 
                           float(Feature_420), float(Feature_421), float(Feature_422), float(Feature_423), 
                           float(Feature_424), float(Feature_425), float(Feature_426), float(Feature_427), 
                           float(Feature_428), float(Feature_429), float(Feature_430), float(Feature_431), 
                           float(Feature_432), float(Feature_433), float(Feature_434), float(Feature_435), 
                           float(Feature_436), float(Feature_437), float(Feature_438), float(Feature_439), 
                           float(Feature_440), float(Feature_441), float(Feature_442), float(Feature_443), 
                           float(Feature_444), float(Feature_445), float(Feature_446), float(Feature_447), 
                           float(Feature_448), float(Feature_449), float(Feature_450), float(Feature_451), 
                           float(Feature_452), float(Feature_453), float(Feature_454), float(Feature_455), 
                           float(Feature_456), float(Feature_457), float(Feature_458), float(Feature_459), 
                           float(Feature_460), float(Feature_461), float(Feature_462), float(Feature_463), 
                           float(Feature_464), float(Feature_465), float(Feature_466), float(Feature_467), 
                           float(Feature_468), float(Feature_469), float(Feature_470), float(Feature_471), 
                           float(Feature_472), float(Feature_473), float(Feature_474), float(Feature_475), 
                           float(Feature_476), float(Feature_477), float(Feature_478), float(Feature_479), 
                           float(Feature_480), float(Feature_481), float(Feature_482), float(Feature_483), 
                           float(Feature_484), float(Feature_485), float(Feature_486), float(Feature_487), 
                           float(Feature_488), float(Feature_489), float(Feature_490), float(Feature_491), 
                           float(Feature_493), float(Feature_494), float(Feature_495), 
                           float(Feature_496), float(Feature_497), float(Feature_498), float(Feature_499), 
                           float(Feature_500), float(Feature_501), float(Feature_502), float(Feature_503), 
                           float(Feature_504), float(Feature_505), float(Feature_506), float(Feature_507), 
                           float(Feature_508), float(Feature_509), float(Feature_510), float(Feature_511), 
                           float(Feature_512), float(Feature_513), float(Feature_514), float(Feature_515), 
                           float(Feature_520), float(Feature_521), float(Feature_522), float(Feature_523), 
                           float(Feature_524), float(Feature_525), float(Feature_526), float(Feature_527), 
                           float(Feature_528), float(Feature_529), float(Feature_530), float(Feature_531), 
                           float(Feature_532), float(Feature_533), float(Feature_534), float(Feature_535), 
                           float(Feature_536), float(Feature_537), float(Feature_538), float(Feature_539), 
                           float(Feature_540), float(Feature_541), float(Feature_542), float(Feature_543), 
                           float(Feature_544), float(Feature_545), float(Feature_546), float(Feature_547), 
                           float(Feature_548), float(Feature_549), float(Feature_550), float(Feature_551), 
                           float(Feature_552), float(Feature_553), float(Feature_554), float(Feature_555), 
                           float(Feature_556), float(Feature_557), float(Feature_558), float(Feature_559), 
                           float(Feature_560), float(Feature_561), float(Feature_562), float(Feature_563), 
                           float(Feature_564), float(Feature_565), float(Feature_566), float(Feature_567), 
                           float(Feature_568), float(Feature_569), float(Feature_570), float(Feature_571), 
                           float(Feature_572), float(Feature_573), float(Feature_574), float(Feature_575), 
                           float(Feature_576), float(Feature_577), float(Feature_582), float(Feature_583), 
                           float(Feature_584), float(Feature_585), float(Feature_586), float(Feature_587), 
                           float(Feature_588), float(Feature_589), int(Month), int(Date), int(Week_Day), 
                           int(Hour), int(Minute)]])
    
    if result==1:
        data="The manufactured semiconductor device is malfunctioning"
    else:
        data="The manufactured semiconductor device is working in a perfectly fine condition"

    return data

# run the application
app.run('0.0.0.0',port='8090')

