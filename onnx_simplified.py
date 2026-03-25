from onnxsim import simplify
import onnx

onnx_path = "./resultve2.onnx"
onnx_simplified_path = "./e2e_simplified.onnx"

# 加载原始 ONNX 模型
onnx_model = onnx.load(onnx_path)

# 简化 ONNX 结构
model_simp, check = simplify(onnx_model)

if check:
    print("✅ ONNX 模型优化成功！")
    onnx.save(model_simp, onnx_simplified_path)
else:
    print("❌ ONNX 模型优化失败，请检查模型结构！")
