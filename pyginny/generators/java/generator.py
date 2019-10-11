"""Java generator"""

from pyginny.models.base_generator import BaseGenerator
from pyginny.models.util.file_util import FileUtil


class Generator(BaseGenerator):
    def process_record_item(self, record):
        result = ""

        # package
        result += "package {0}".format(self.get_option("--java-package"))
        result += self.get_nl() + self.get_nl()

        # class name
        result += "public final class {0}".format(record.name.capitalize())
        result += " {"
        result += self.get_nl() + self.get_nl()

        # field
        for field in record.fields:
            result += "{0}protected {1} {2};".format(
                self.get_indent(), self.get_java_type(field.type), field.name
            )

            result += self.get_nl() + self.get_nl()

        # getter
        for field in record.fields:
            result += "{0}public {1} get{2}()".format(
                self.get_indent(),
                self.get_java_type(field.type),
                field.name.capitalize(),
            )

            result += " {"
            result += self.get_nl()

            result += "{0}return this.{1};".format(
                (self.get_indent() + self.get_indent()), field.name
            )

            result += self.get_nl()
            result += self.get_indent() + "}"
            result += self.get_nl() + self.get_nl()

        result += "}"

        return result

    def process_record_list(self):
        output_path = self.get_output_path()

        for record in self.model.records:
            filename = "{0}.java".format(record.name.capitalize())
            file_content = self.process_record_item(record=record)
            FileUtil.write_to_file(output_path, filename, file_content)

    def get_usage_options(self):
        result = ""
        result += "Generator Java:\n"
        result += "  --java-out VALUE                              The output for the Java files (Generator disabled if unspecified).\n"
        result += "  --java-package VALUE                          The package name to use for generated Java classes.\n"
        result += "  --java-class-access-modifier VALUE            The access modifier to use for generated Java classes (default: public).\n"
        result += "  --java-cpp-exception VALUE                    The type for translated C++ exceptions in Java (default: java.lang.RuntimeException that is not checked)\n"
        result += "  --java-annotation VALUE                       Java annotation (@Foo) to place on all generated Java classes\n"
        result += "  --java-generate-interfaces VALUE              Whether Java interfaces should be used instead of abstract classes where possible (default: false).\n"
        result += "  --java-nullable-annotation VALUE              Java annotation (@Nullable) to place on all fields and return values that are optional\n"
        result += "  --java-nonnull-annotation VALUE               Java annotation (@Nonnull) to place on all fields and return values that are not optional\n"
        result += "  --java-implement-android-os-parcelable VALUE  All generated java classes will implement the interface android.os.Parcelable\n"
        result += "  --java-use-final-for-record VALUE             Whether generated Java classes for records should be marked 'final' (default: true)."

        return result

    def get_name(self):
        return "java"

    def get_output_path(self):
        if "--java-out" in self.options:
            if self.options["--java-out"]:
                return self.options["--java-out"]

        return None

    def can_run(self):
        if self.get_output_path():
            return True

        return False

    def get_java_type(self, value):
        if type(value).__name__ == "SimpleType":
            value = value.name

            if value == "bool":
                return "Boolean"
            elif value == "string":
                return "String"
            elif value == "i8":
                return "Integer"
            elif value == "i16":
                return "int"
            elif value == "i32":
                return "int"
            elif value == "i64":
                return "long"
            elif value == "f32":
                return "Float"
            elif value == "f64":
                return "Float"
            elif value == "binary":
                return "byte[]"
            elif value == "date":
                return "java.util.Date"

        return None
